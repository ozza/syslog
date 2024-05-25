from pyparsing import *
from app.helpers import hash_helper
import datetime


def nat_parser(data_to_parse):
    out = []
    inn = str(data_to_parse).split(']:')

    header = inn[0].split(' ')

    out.append(header[0][7:])
    out.append(header[1])
    out.append(header[2])
    out.append(header[3])

    value = Literal('<').suppress() + SkipTo('>')

    for k in value.searchString(inn[1]):
        out.append(str(k).strip('[').strip(']').strip("'"))

    out.append(data_to_parse)
    out.append(hash_helper.hasher(data_to_parse))

    return out
