import datetime
import elasticsearch
from app.helpers import mac_finder
from dateutil.parser import parse


def get_mac(es, index, packet_type, irange, ip):
    mac = mac_finder.get_last_mac_of_an_ip_address(es, index, packet_type, irange, ip)
    return mac


def nat_db_writer(es, index, log_data, iid, qsize):
    mac = get_mac(es, index, 'ar_dhcp', '1M', str(log_data[8]).split(':')[0])

    doc = {
        'iid': iid,
        'Timestamp': datetime.datetime.now(),
        'Date': parse(str(log_data[0])).date(),
        'Time_FW': log_data[1],
        'DeviceName': log_data[2],
        'LogType': log_data[3],
        'Protocol': log_data[4],
        'Operator': log_data[5],
        'IpVersion': log_data[6],
        'IPv4Tos': log_data[7],
        'from': log_data[8],
        'to': log_data[9],
        'SourceNat': log_data[10],
        'DestNat': log_data[11],
        'begin_time': log_data[12],
        'end_time': log_data[13],
        'time_of_duration': log_data[14],
        'PosTotalPkg': log_data[15],
        'PosTotalByte': log_data[16],
        'NegTotalPkg': log_data[17],
        'NegTotalByte': log_data[18],
        'Data': str(log_data[19]),
        'Hash': log_data[20],
        'qsize': qsize,
        'MacAddress': mac if mac != 0 else ""
    }
    try:
        es.index(index=index, doc_type="nat", body=doc)
    # except elasticsearch.exceptions.ConflictError as ex:
    #     es.delete(index=index, doc_type="cm", id=iid)
    #     es.create(index=index, doc_type="cm", id=iid, body=doc)
    #     raise ex
    # except elasticsearch.exceptions.ConnectionTimeout as ex:
    #     raise ex
    # except elasticsearch.exceptions.ConnectionError as ex:
    #     raise ex
    # except elasticsearch.exceptions.RequestError as ex:
    #     raise ex
    # except elasticsearch.exceptions.TransportError as ex:
    #     raise ex
    except Exception as ex:
        raise ex
