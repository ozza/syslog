import datetime
import elasticsearch
from dateutil.parser import parse


def hwcm_db_writer(es, index, log_data, iid, qsize):
    doc = {
        'iid': iid,
        'Timestamp': datetime.datetime.now(),
        'Date': parse(str(log_data[0])).date(),
        'Time_FW': log_data[1],
        'DeviceName': log_data[2],
        'LogType': log_data[3],
        'OID': log_data[4],
        'EventIndex': log_data[5],
        'CommandSource': log_data[6],
        'ConfigSource': log_data[7],
        'ConfigDestination': log_data[8],
        'Data': str(log_data[9]),
        'Hash': log_data[10],
        'qsize': qsize
    }
    try:
        es.index(index=index, doc_type="hwcm", body=doc)
    # except elasticsearch.exceptions.ConflictError as ex:
    #     es.delete(index=index, doc_type="hwcm", id=iid)
    #     es.create(index=index, doc_type="hwcm", id=iid, body=doc)
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
