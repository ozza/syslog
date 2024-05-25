from pyparsing import *
from app.helpers import hash_helper
import datetime


def ar_dhcp_parser(data_to_parse):
    out = []
    inn = str(data_to_parse).split('(l)')

    header = inn[0].split(' ')

    out.append(header[0][7:])
    out.append(header[1])
    out.append(header[2])
    out.append(header[3])

    eq = Literal("=").suppress()
    comma = Literal(",").suppress()

    key = Word(alphas, alphanums)
    value = quotedString | Word(printables) | Word(alphas) | Word(alphanums) | key
    tot = key.setResultsName("key") + "=" + value.setResultsName("value")

    for t, s, e in tot.scanString(inn[1]):
        out.append(str(t.value).strip('"').strip(',').strip("'").strip('(').strip(')'))

    out.append(data_to_parse)
    out.append(hash_helper.hasher(data_to_parse))

    return out