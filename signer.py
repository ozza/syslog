#!/usr/bin/python3.6

import os
import time
import subprocess
import tarfile
import datetime
import shutil
import configparser

FNULL = open(os.devnull, "w")


def remove_files(dirpath):
    for filename in os.listdir(dirpath):
        filepath = os.path.join(dirpath, filename)
        try:
            shutil.rmtree(filepath)
        except OSError:
            os.remove(filepath)


def sign_and_archive_files(work_dir):
    try:
        for file_namee in os.listdir(work_dir):
            if (
                ".log" in str(file_namee)
                and str(datetime.date.today()) not in str(file_namee)
                and "error" not in str(file_namee)
            ):
                file_name = str(file_namee.split(".")[0])
                if not os.path.isfile(work_dir + "signed/" + file_name + ".tar.gz"):
                    shutil.copy(
                        work_dir + file_name + ".log",
                        work_dir + "progress/" + file_name + ".log",
                    )
                    time.sleep(10)

                    try:
                        subprocess.check_call(
                            [
                                "openssl",
                                "ts",
                                "-query",
                                "-data",
                                work_dir + "progress/" + file_name + ".log",
                                "-no_nonce",
                                "-out",
                                work_dir + "progress/" + file_name + ".tsq",
                            ],
                            stdout=FNULL,
                            stderr=subprocess.STDOUT,
                        )
                        time.sleep(10)
                    except Exception as ex:
                        log_file = open(work_dir + "error_sign.log", "a")
                        log_file.write(
                            str(datetime.datetime.now())
                            + " ERROR: "
                            + str(ex)
                            + "\n--------------------------------\n"
                        )
                        log_file.close()
                        remove_files(work_dir + "progress")

                    try:
                        subprocess.check_call(
                            [
                                "openssl",
                                "ts",
                                "-reply",
                                "-queryfile",
                                work_dir + "progress/" + file_name + ".tsq",
                                "-out",
                                work_dir + "progress/" + file_name + ".der",
                                "-token_out",
                                "-config",
                                OpenSSLConfig,
                                "-passin",
                                "pass:" + password,
                            ],
                            stdout=FNULL,
                            stderr=subprocess.STDOUT,
                        )
                        time.sleep(10)
                    except Exception as ex:
                        log_file = open(work_dir + "error_sign.log", "a")
                        log_file.write(
                            str(datetime.datetime.now())
                            + " ERROR: "
                            + str(ex)
                            + "\n--------------------------------\n"
                        )
                        log_file.close()
                        remove_files(work_dir + "progress")

                    proc = subprocess.check_output(
                        [
                            "openssl",
                            "ts",
                            "-verify",
                            "-data",
                            work_dir + "progress/" + file_name + ".log",
                            "-in",
                            work_dir + "progress/" + file_name + ".der",
                            "-token_in",
                            "-CAfile",
                            CAKey,
                            "-untrusted",
                            TSAKey,
                        ]
                    )  # , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    time.sleep(10)

                    if "Verification: OK" in str(proc, "utf-8").rstrip():
                        tar = tarfile.open(file_name + ".tar.gz", "w:gz")
                        tar.add(
                            work_dir + "progress/" + file_name + ".log",
                            file_name + ".log",
                        )
                        tar.add(
                            work_dir + "progress/" + file_name + ".der",
                            file_name + ".der",
                        )
                        tar.add(
                            work_dir + "progress/" + file_name + ".tsq",
                            file_name + ".tsq",
                        )
                        tar.close()

                        shutil.move(
                            file_name + ".tar.gz",
                            work_dir + "signed/" + file_name + ".tar.gz",
                        )
                        remove_files(work_dir + "progress")

                        # To remove files, uncomment below
                        os.remove(work_dir + file_name + ".log")
                    else:
                        tar = tarfile.open(file_name + ".tar.gz", "w:gz")
                        if os.path.isfile(work_dir + file_name + ".log"):
                            tar.add(
                                work_dir + "progress/" + file_name + ".log",
                                file_name + ".log",
                            )
                        if os.path.isfile(work_dir + file_name + ".der"):
                            tar.add(
                                work_dir + "progress/" + file_name + ".der",
                                file_name + ".der",
                            )
                        if os.path.isfile(work_dir + file_name + ".tsq"):
                            tar.add(
                                work_dir + "progress/" + file_name + ".tsq",
                                file_name + ".tsq",
                            )
                        tar.close()

                        shutil.move(
                            file_name + ".tar.gz",
                            work_dir + "error/" + file_name + ".tar.gz",
                        )
                        remove_files(work_dir + "progress")

                        # To remove files, uncomment below
                        # os.remove(work_dir + file_name + ".log")

                        log_file = open(work_dir + "error_sign.log", "a")
                        log_file.write(
                            str(datetime.datetime.now())
                            + " ERROR: Doğrulama Hatası ("
                            + str(proc, "utf-8").rstrip()
                            + "\n--------------------------------\n"
                        )
                        log_file.close()
    except Exception as ex:
        log_file = open(work_dir + "error_sign.log", "a")
        log_file.write(
            str(datetime.datetime.now())
            + " ERROR: "
            + str(ex)
            + "\n--------------------------------\n"
        )
        log_file.close()


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config.ini")

    CAKey = config["SIGNER"]["CAKey"]
    TSAKey = config["SIGNER"]["TSAKey"]

    OpenSSLConfig = config["SIGNER"]["OpenSSLConfig"]
    password = config["SIGNER"]["Password"]

    for ports in config["PORTMAPPINGS"]:
        mapping = str(config["PORTMAPPINGS"][ports]).split(",")

        work_dir1 = config["SIGNER"]["WorkingDirectory"] + str(mapping[1]) + "/"

        sign_and_archive_files(work_dir1)
