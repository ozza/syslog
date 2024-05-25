import multiprocessing as mp
import datetime

from app.helpers import file_helper, error_helper


class LogWriter(mp.Process):
    def __init__(self, wqueue, index, logdir, devlogdir, devicelist):
        mp.Process.__init__(self)
        self.wqueue = wqueue
        self.log_dir = logdir + index + "/"
        self.device_log_dir = devlogdir
        self.index = index
        self.device_list = devicelist

        self.log_file = str(self.log_dir + "logs/UNKNOWN.log")
        self.log_file_audit = str(self.log_dir + "logs/AUDIT.log")
        self.log_file_url = str(self.log_dir + "logs/URL.log")
        self.log_file_ppermit = str(self.log_dir + "logs/PPERMIT.log")
        self.log_file_pdeny = str(self.log_dir + "logs/PDENY.log")
        self.log_file_session = str(self.log_dir + "logs/SES.log")
        self.log_file_dhcp = str(self.log_dir + "logs/DHCP.log")
        self.log_file_um = str(self.log_dir + "logs/UM.log")
        self.log_file_cm = str(self.log_dir + "logs/CM.log")
        self.log_file_hwcm = str(self.log_dir + "logs/HWCM.log")
        self.log_file_errors = str(self.log_dir + "logs/ERROR.log")
        self.log_file_ar_dhcp = self.log_dir + "logs/ARDHCP.log"
        self.log_file_nat = self.log_dir + "logs/NAT.log"

    def writer(self, all_data):
        data = str(all_data[0])
        ip = str(all_data[1][0])

        if any(str(ip) in s for s in self.device_list.values()):
            file_helper.file_inserter(
                data,
                str(
                    list(self.device_list.keys())[
                        list(self.device_list.values()).index(str(ip))
                    ]
                ),
                self.device_log_dir,
            )

        if "SESSION_TEARDOWN(l)" in str(data):
            try:
                file_helper.file_inserter(data, "SES", self.log_dir)

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_session,
                    datetime.datetime.now(),
                    "SESSION_TEARDOWN",
                    ex,
                    data,
                )

        elif "POLICYPERMIT(l)" in str(data):
            try:
                file_helper.file_inserter(data, "PPERMIT", self.log_dir)

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_ppermit,
                    datetime.datetime.now(),
                    "POLICY_PERMIT",
                    ex,
                    data,
                )

        elif "POLICYDENY(l)" in str(data):
            try:
                file_helper.file_inserter(data, "PDENY", self.log_dir)

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_pdeny,
                    datetime.datetime.now(),
                    "POLICY_DENY",
                    ex,
                    data,
                )

        elif "01AUDIT" in str(data):
            try:
                file_helper.file_inserter(data, "AUDIT", self.log_dir)

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_audit, datetime.datetime.now(), "AUDIT", ex, data
                )

        elif "01URL" in str(data):
            try:
                file_helper.file_inserter(data, "URL", self.log_dir)

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_url, datetime.datetime.now(), "URL", ex, data
                )

        elif "01UM" in str(data):
            try:
                file_helper.file_inserter(data, "UM", self.log_dir)

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_um, datetime.datetime.now(), "UM", ex, data
                )

        elif "01CM" in str(data):
            try:
                file_helper.file_inserter(data, "CM", self.log_dir)

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_cm, datetime.datetime.now(), "CM", ex, data
                )

        elif "HWCM" in str(data):
            try:
                file_helper.file_inserter(data, "HWCM", self.log_dir)

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_hwcm, datetime.datetime.now(), "HWCM", ex, data
                )

        elif (
            ",Renew," in str(data)
            or ",Assign," in str(data)
            or ",Deleted," in str(data)
        ):
            try:
                file_helper.file_inserter(data, "DHCP", self.log_dir)

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_dhcp, datetime.datetime.now(), "DHCP", ex, data
                )

        elif "IPALLOCOK(l)" in str(data):
            try:
                file_helper.file_inserter(data, "ARDHCP", self.log_dir)

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_ar_dhcp, datetime.datetime.now(), "ARDHCP", ex, data
                )

        elif "%%01FW-LOG/5/SESSION_LOG(l)" in str(data):
            try:
                file_helper.file_inserter(data, "NAT", self.log_dir)

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_nat, datetime.datetime.now(), "NAT", ex, data
                )

        else:
            error_helper.error_logger(
                self.log_file, datetime.datetime.now(), "UNKNOWN DATA", "", data
            )

    def run(self):
        pool = mp.Pool(5)
        manager = mp.Manager()

        while 1:
            data = self.wqueue.get()

            if data:
                work_pool = pool.apply_async(self.writer(data))
