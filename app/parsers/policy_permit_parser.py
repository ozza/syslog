import re
import datetime

from app.helpers import hash_helper


def policy_permit_parser(data_to_parse):
    out = []
    inn = str(data_to_parse).split('):')

    phys_props = inn[0].split(' ')

    if str(phys_props[1]) == "":
        out.append(
            datetime.datetime.strptime(phys_props[0][7:] + " " + phys_props[2] + " " + phys_props[3], "%b %d %Y").date())
        out.append(phys_props[4])
        out.append(phys_props[5])
        out.append(phys_props[6] + ")")
    else:
        out.append(datetime.datetime.strptime(phys_props[0][7:] + " " + phys_props[1] + " " + phys_props[2], "%b %d %Y").date())

        out.append(phys_props[3])
        out.append(phys_props[4])
        out.append(phys_props[5] + ")")

    properties = re.findall(r"((?:\".*?\")|=[\w][^,]+|=[\w])", inn[1])

    out.append(properties[0][1:])
    out.append(properties[1][1:])
    out.append(properties[2][1:])
    out.append(properties[3][1:])
    out.append(properties[4][1:])
    out.append(properties[5][1:])
    out.append(properties[6][1:])
    out.append(properties[7][1:])
    out.append(properties[8][1:])
    out.append(properties[9][1:])

    out.append(data_to_parse)
    out.append(hash_helper.hasher(data_to_parse))

    return out
