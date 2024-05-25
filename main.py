#!/usr/bin/python3.6

import configparser
import multiprocessing as mp
import time
import datetime

from elasticsearch import *

from app import cli_consumer_huawei, cli_listener, cli_log_writer
from app.helpers import file_helper, error_helper

import settings

if __name__ == "__main__":

    config = configparser.ConfigParser()
    config.read("config.ini")

    pool_size = config["ELASTICSEARCH"]["PoolSize"]

    processes = []
    threads = []

    try:
        elasticsrc = Elasticsearch(
            [config["ELASTICSEARCH"]["Host"]],
            timeout=30,
            maxsize=int(pool_size),
            retry_on_timeout=True,
            max_retries=100,
        )

        server_status = 0

        while server_status == 0:
            if (
                elasticsrc.cluster.health()["status"] == "yellow"
                or elasticsrc.cluster.health()["status"] == "green"
            ):
                server_status = 1
            else:
                time.sleep(10)

        for ports in config["PORTMAPPINGS"]:
            mapping = str(config["PORTMAPPINGS"][ports]).split(",")

            rqueue = mp.Queue()
            wqueue = mp.Queue()

            conf = settings.Config(elasticsrc, str(mapping[1]))

            proc_listener = cli_listener.UdpListener(
                rqueue,
                config["LISTENER"]["Host"],
                int(mapping[0]),
                int(config["LISTENER"]["Buffer"]),
            )
            proc_cli_log_writer = cli_log_writer.LogWriter(
                wqueue,
                str(mapping[1]),
                config["LOG"]["LogDirectory"],
                config["LOG"]["DeviceLogDirectory"],
                config["DEVICES"],
            )

            proc_listener.start()
            processes.append(proc_listener)
            proc_cli_log_writer.start()
            processes.append(proc_cli_log_writer)

            threads = [
                cli_consumer_huawei.Consumer(
                    rqueue,
                    wqueue,
                    str(mapping[1]),
                    config["LOG"]["LogDirectory"],
                    elasticsrc,
                    conf,
                )
                for _ in range(int(mapping[2]))
            ]

            [t.start() for t in threads]

        [p.join() for p in processes]
        [t.join() for t in threads]

    except KeyboardInterrupt:
        for p in processes:
            p.terminate()

    except Exception as ex:
        file_helper.file_inserter(ex, "MAIN", config["LOG"]["LogDirectory"])

    finally:
        for p in processes:
            p.terminate()
