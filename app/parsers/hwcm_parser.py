from pyparsing import *
from app.helpers import hash_helper
import datetime


def hwcm_parser(data_to_parse):
    out = []
    inn = str(data_to_parse).split(":O")
    inn[1] = "O{0}".format(inn[1])

    phys_props = inn[0].split(" ")
    out.append(
        datetime.datetime.strptime(
            phys_props[0][7:] + " " + phys_props[1] + " " + phys_props[2], "%b %d %Y"
        ).date()
    )
    out.append(phys_props[3])
    out.append(phys_props[4])
    out.append(phys_props[5].split("(s)")[0])

    key = Word(alphas, alphanums)
    value = quotedString | Word(printables) | Word(alphas) | Word(alphanums) | key
    tot = key.setResultsName("key") + "=" + value.setResultsName("value")
    oid = Literal("OID") + SkipTo("(")

    out.append(
        str(oid.searchString(inn[1]))
        .strip("[")
        .strip("]")
        .strip("'")
        .replace("', '", " ")
    )

    for t, s, e in tot.scanString(inn[1]):
        out.append(str(t.value).strip('"').strip(",").strip("'").strip("(").strip(")"))

    out.append(data_to_parse)
    out.append(hash_helper.hasher(data_to_parse))

    return out
