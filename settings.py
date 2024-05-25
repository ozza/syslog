from app.helpers import id_finder


class Config(object):
    def __init__(self, es, index):
        self.session_id = id_finder.get_latest_id(es, index, "session_teardown", "30d")
        self.audit_id = id_finder.get_latest_id(es, index, "audit", "30d")
        self.url_id = id_finder.get_latest_id(es, index, "url", "30d")
        self.dhcp_id = id_finder.get_latest_id(es, index, "dhcp", "30d")
        self.pdeny_id = id_finder.get_latest_id(es, index, "policy_deny", "30d")
        self.ppermit_id = id_finder.get_latest_id(es, index, "policy_permit", "30d")
        self.cm_id = id_finder.get_latest_id(es, index, "cm", "30d")
        self.hwcm_id = id_finder.get_latest_id(es, index, "hwcm", "30d")
        self.um_id = id_finder.get_latest_id(es, index, "um", "30d")
        self.ardhcp_id = id_finder.get_latest_id(es, index, "ar_dhcp", "30d")
        self.nat_id = id_finder.get_latest_id(es, index, "nat", "30d")

    def session_current(self):
        current = self.session_id
        self.session_id += 1

        return current

    def session_decrease(self):
        self.session_id -= 1

    def audit_current(self):
        current = self.audit_id
        self.audit_id += 1

        return current

    def audit_decrease(self):
        self.audit_id -= 1

    def url_current(self):
        current = self.url_id
        self.url_id += 1

        return current

    def url_decrease(self):
        self.url_id -= 1

    def dhcp_current(self):
        current = self.dhcp_id
        self.dhcp_id += 1

        return current

    def dhcp_decrease(self):
        self.dhcp_id -= 1

    def pdeny_current(self):
        current = self.pdeny_id
        self.pdeny_id += 1

        return current

    def pdeny_decrease(self):
        self.pdeny_id -= 1

    def ppermit_current(self):
        current = self.ppermit_id
        self.ppermit_id += 1

        return current

    def ppermit_decrease(self):
        self.ppermit_id -= 1

    def cm_current(self):
        current = self.cm_id
        self.cm_id += 1

        return current

    def cm_decrease(self):
        self.cm_id -= 1

    def hwcm_current(self):
        current = self.hwcm_id
        self.hwcm_id += 1

        return current

    def hwcm_decrease(self):
        self.hwcm_id -= 1

    def um_current(self):
        current = self.um_id
        self.um_id += 1

        return current

    def um_decrease(self):
        self.um_id -= 1

    def ardhcp_current(self):
        current = self.ardhcp_id
        self.ardhcp_id += 1

        return current

    def ardhcp_decrease(self):
        self.ardhcp_id -= 1

    def nat_current(self):
        current = self.nat_id
        self.nat_id += 1

        return current

    def nat_decrease(self):
        self.nat_id -= 1