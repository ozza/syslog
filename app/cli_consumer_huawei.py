import datetime
import threading as thread

from app.parsers import (
    policy_permit_parser,
    audit_parser,
    dhcp_parser,
    policy_deny_parser,
    session_td_parser,
    url_parser,
    cm_parser,
    hwcm_parser,
    um_parser,
    ar_dhcp_parser,
    nat_parser,
)
from app.db_writers.microsoft import dhcp_db_writer
from app.db_writers.huawei import (
    policy_permit_db_writer,
    policy_deny_db_writer,
    session_td_db_writer,
    url_db_writer,
    audit_db_writer,
    cm_db_writer,
    hwcm_db_writer,
    um_db_writer,
    ar_dhcp_db_writer,
    nat_db_writer,
)
from app.helpers import error_helper
import settings


class Consumer(thread.Thread):
    def __init__(self, rqueue, wqueue, index, logdir, elastic, ids):
        thread.Thread.__init__(self)
        self.rqueue = rqueue
        self.wqueue = wqueue
        self.es = elastic
        self.index = index
        self.log_dir = logdir + index + "/"
        self.ids = ids

        self.log_file = self.log_dir + "logs/UNKNOWN.log"
        self.log_file_audit = self.log_dir + "logs/AUDIT.log"
        self.log_file_url = self.log_dir + "logs/URL.log"
        self.log_file_ppermit = self.log_dir + "logs/PPERMIT.log"
        self.log_file_pdeny = self.log_dir + "logs/PDENY.log"
        self.log_file_session = self.log_dir + "logs/SES.log"
        self.log_file_dhcp = self.log_dir + "logs/DHCP.log"
        self.log_file_cm = self.log_dir + "logs/CM.log"
        self.log_file_um = self.log_dir + "logs/UM.log"
        self.log_file_hwcm = self.log_dir + "logs/HWCM.log"
        self.log_file_errors = self.log_dir + "logs/ERROR.log"
        self.log_file_ar_dhcp = self.log_dir + "logs/ARDHCP.log"
        self.log_file_nat = self.log_dir + "logs/NAT.log"

    def consume(self, data, size):
        if "SESSION_TEARDOWN(l)" in str(data):
            try:
                iid = settings.Config.session_current(self.ids)
                session_td_db_writer.session_td_db_writer(
                    self.es,
                    self.index,
                    session_td_parser.session_td_parser(data),
                    iid,
                    size,
                )

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_session,
                    datetime.datetime.now(),
                    "SESSION_TEARDOWN",
                    ex,
                    data,
                )
                settings.Config.session_decrease(self.ids)

        elif "POLICYPERMIT(l)" in str(data):
            try:
                iid = settings.Config.ppermit_current(self.ids)
                policy_permit_db_writer.policy_permit_db_writer(
                    self.es,
                    self.index,
                    policy_permit_parser.policy_permit_parser(data),
                    iid,
                    size,
                )

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_ppermit,
                    datetime.datetime.now(),
                    "POLICY_PERMIT",
                    ex,
                    data,
                )
                settings.Config.ppermit_decrease(self.ids)

        elif "POLICYDENY(l)" in str(data):
            try:
                iid = settings.Config.pdeny_current(self.ids)
                policy_deny_db_writer.policy_deny_db_writer(
                    self.es,
                    self.index,
                    policy_deny_parser.policy_deny_parser(data),
                    iid,
                    size,
                )

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_pdeny,
                    datetime.datetime.now(),
                    "POLICY_DENY",
                    ex,
                    data,
                )
                settings.Config.pdeny_decrease(self.ids)

        elif "01AUDIT" in str(data):
            try:
                iid = settings.Config.audit_current(self.ids)
                audit_db_writer.audit_db_writer(
                    self.es, self.index, audit_parser.audit_parser(data), iid, size
                )

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_audit, datetime.datetime.now(), "AUDIT", ex, data
                )
                settings.Config.audit_decrease(self.ids)

        elif "01URL" in str(data):
            try:
                iid = settings.Config.url_current(self.ids)
                url_db_writer.url_db_writer(
                    self.es, self.index, url_parser.url_parser(data), iid, size
                )

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_url, datetime.datetime.now(), "URL", ex, data
                )
                settings.Config.url_decrease(self.ids)

        elif "01UM" in str(data):
            try:
                iid = settings.Config.um_current(self.ids)
                um_db_writer.um_db_writer(
                    self.es, self.index, um_parser.um_parser(data), iid, size
                )

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_um, datetime.datetime.now(), "UM", ex, data
                )
                settings.Config.um_decrease(self.ids)

        elif "01CM" in str(data):
            try:
                iid = settings.Config.cm_current(self.ids)
                cm_db_writer.cm_db_writer(
                    self.es, self.index, cm_parser.cm_parser(data), iid, size
                )

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_cm, datetime.datetime.now(), "CM", ex, data
                )
                settings.Config.cm_decrease(self.ids)

        elif "HWCM" in str(data):
            try:
                iid = settings.Config.hwcm_current(self.ids)
                hwcm_db_writer.hwcm_db_writer(
                    self.es, self.index, hwcm_parser.hwcm_parser(data), iid, size
                )

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_hwcm, datetime.datetime.now(), "HWCM", ex, data
                )
                settings.Config.hwcm_decrease(self.ids)

        elif (
            ",Renew," in str(data)
            or ",Assign," in str(data)
            or ",Deleted," in str(data)
        ):
            try:
                iid = settings.Config.dhcp_current(self.ids)
                dhcp_db_writer.dhcp_db_writer(
                    self.es, self.index, dhcp_parser.dhcp_parser(data), iid, size
                )

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_dhcp, datetime.datetime.now(), "DHCP", ex, data
                )
                settings.Config.dhcp_decrease(self.ids)

        elif "IPALLOCOK(l)" in str(data):
            try:
                iid = settings.Config.ardhcp_current(self.ids)
                ar_dhcp_db_writer.ar_dhcp_db_writer(
                    self.es, self.index, ar_dhcp_parser.ar_dhcp_parser(data), iid, size
                )

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_ar_dhcp, datetime.datetime.now(), "ARDHCP", ex, data
                )
                settings.Config.ardhcp_decrease(self.ids)

        elif "%%01FW-LOG/5/SESSION_LOG(l)" in str(data):
            try:
                iid = settings.Config.nat_current(self.ids)
                nat_db_writer.nat_db_writer(
                    self.es, self.index, nat_parser.nat_parser(data), iid, size
                )

            except Exception as ex:
                error_helper.error_logger(
                    self.log_file_nat, datetime.datetime.now(), "NAT", ex, data
                )
                settings.Config.nat_decrease(self.ids)

        else:
            error_helper.error_logger(
                self.log_file, datetime.datetime.now(), "UNKNOWN DATA", "", data
            )

    def run(self):
        while 1:
            size = self.rqueue.qsize()

            if int(size) >= 0:
                all_data = self.rqueue.get()
                self.wqueue.put(all_data)

                data = str(all_data[0])

                self.consume(data, size)
