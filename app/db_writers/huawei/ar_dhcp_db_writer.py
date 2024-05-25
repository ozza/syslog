import datetime
import elasticsearch
from dateutil.parser import parse


def ar_dhcp_db_writer(es, index, log_data, iid, qsize):
    doc = {
        'iid': iid,
        'Timestamp': datetime.datetime.now(),
        'Date': parse(str(log_data[0])).date(),
        'Time_FW': log_data[1],
        'DeviceName': log_data[2],
        'LogType': log_data[3],
        'PoolName': log_data[4],
        'MacAddress': log_data[5],
        'IpAddress': log_data[6],
        'LeaseTime': log_data[7],
        'Data': str(log_data[8]),
        'Hash': log_data[9],
        'qsize': qsize
    }
    try:
        es.index(index=index, doc_type="ar_dhcp", body=doc)
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