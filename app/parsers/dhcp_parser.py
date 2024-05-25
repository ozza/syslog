from app.helpers import hash_helper
import datetime


def dhcp_parser(data_to_parse):
    out = []
    inn = str("%r" % data_to_parse).split(',')

    out.append(inn[0][2:])
    out.append(str(datetime.datetime.strptime(inn[1], '%m/%d/%y').date()))
    out.append(inn[2])
    out.append(inn[3])
    out.append(inn[4])
    out.append(inn[5])
    out.append(inn[6])
    out.append(inn[7])
    out.append(inn[8])

    out.append(str(data_to_parse))
    out.append(hash_helper.hasher(data_to_parse))

    return out
