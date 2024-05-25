import datetime
import elasticsearch
from dateutil.parser import parse


def policy_deny_db_writer(es, index, log_data, iid, qsize):
    doc = {
        'iid': iid,
        'Timestamp': datetime.datetime.now(),
        'Date': parse(str(log_data[0])).date(),
        'Time_FW': log_data[1],
        'DeviceName': log_data[2],
        'LogType': log_data[3],
        'Vsys': log_data[4],
        'Protocol': log_data[5],
        'Source-ip': log_data[6],
        'Source-port': log_data[7],
        'Destination-ip': log_data[8],
        'Destination-port': log_data[9],
        'Time': log_data[10],
        'Source-zone': log_data[11],
        'Destination-zone': log_data[12],
        'Rule-name': log_data[13],
        'Data': str(log_data[14]),
        'Hash': log_data[15],
        'qsize': qsize
    }
    try:
        es.index(index=index, doc_type="policy_deny", body=doc)
    # except elasticsearch.exceptions.ConflictError as ex:
    #     es.delete(index=index, doc_type="policy_deny", id=iid)
    #     es.create(index=index, doc_type="policy_deny", id=iid, body=doc)
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
