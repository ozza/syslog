from pyparsing import *
from app.helpers import hash_helper


def um_parser(data_to_parse):
    out = []
    inn = str(data_to_parse).split('):')

    phys_props = inn[0].split(' ')
    out.append(phys_props[0][7:])
    out.append(phys_props[1])
    out.append(phys_props[2])
    out.append(phys_props[3][:-2])

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

