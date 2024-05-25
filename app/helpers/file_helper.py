import datetime
import hashlib
import os


# TODO refactor
def check_date_and_filename(logtype, log_dir):
    now = log_dir + str(logtype) + "_" + str(datetime.date.today()) + ".log"
    if os.path.isfile(now):
        return now
    else:
        filelog = open(now, 'a')
        filelog.close()
        return now


def file_inserter(data, logtype, log_dir):
    syslog_file = check_date_and_filename(logtype, log_dir)
    m = hashlib.md5()
    m.update(str(data).encode())

    file = open(syslog_file, 'a')

    file.write(str(data) + ", md5:" + m.hexdigest() + "\n")
    file.close()
