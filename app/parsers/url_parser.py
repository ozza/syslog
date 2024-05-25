import re

from app.helpers import hash_helper


def url_parser(data_to_parse):
    out = []
    inn = str(data_to_parse).split('matched. (')

    phys_props = inn[0].split(' ')
    out.append(phys_props[0][7:])
    out.append(phys_props[1])
    out.append(phys_props[2])
    out.append(phys_props[3][:-1])

    properties = re.findall(r"((?:\".*?\")|=[\w][^,]+|=[\w])", inn[1])

    out.append(properties[0][1:])
    out.append(properties[1][1:-1])
    out.append(properties[2][1:-1])
    out.append(properties[3][1:])
    out.append(properties[4][1:])
    out.append(properties[5][1:])
    out.append(properties[6][1:])
    out.append(properties[7][1:])
    out.append(properties[8][1:])
    out.append(properties[9][1:-1])
    out.append(properties[10][1:])
    out.append(properties[11][1:-1])
    out.append(properties[12][1:-1])
    out.append(properties[13][1:])
    out.append(properties[14][1:])
    out.append(properties[15][1:-1])
    out.append(properties[16][1:-1])
    out.append(properties[17][1:-1])
    out.append(properties[18][1:-1])
    out.append(properties[19][1:-1])
    out.append(properties[20][1:-2])

    out.append(data_to_parse)
    out.append(hash_helper.hasher(data_to_parse))

    return out
