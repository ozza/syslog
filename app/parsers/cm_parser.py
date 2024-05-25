from pyparsing import *
from app.helpers import hash_helper
import datetime


def cm_parser(data_to_parse):
    if "USER_OFFLINERESULT" in data_to_parse:
        out = []
        inn = str(data_to_parse).split(':[WLAN_STA_INFO_OFFLINE]')

        phys_props = inn[0].split(' ')
        out.append(datetime.datetime.strptime(phys_props[0][7:], "%Y-%m-%d").date())
        out.append(phys_props[1])
        out.append(phys_props[2])
        out.append(phys_props[3].split('(s)')[0])

        value = Literal(':').suppress() + SkipTo(';')

        for k in value.searchString(inn[1]):
            out.append(str(k).strip('[').strip(']').strip("'"))

        out.append(data_to_parse)
        out.append(hash_helper.hasher(data_to_parse))

        return out

    elif "USER_ACCESSRESULT" in data_to_parse:
        out = []
        inn = str(data_to_parse).split(':[WLAN_STA_INFO_AUTHENTICATION]')

        phys_props = inn[0].split(' ')
        out.append(datetime.datetime.strptime(phys_props[0][7:], "%Y-%m-%d").date())
        out.append(phys_props[1])
        out.append(phys_props[2])
        out.append(phys_props[3].split('(s)')[0])

        value = Literal(':').suppress() + SkipTo(';')

        for k in value.searchString(inn[1]):
            out.append(str(k).strip('[').strip(']').strip("'"))

        out.append(data_to_parse)
        out.append(hash_helper.hasher(data_to_parse))

        return out

