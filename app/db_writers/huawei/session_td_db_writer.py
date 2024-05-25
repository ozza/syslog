import datetime
import elasticsearch
from dateutil.parser import parse


def session_td_db_writer(es, index, log_data, iid, qsize):
    doc = {
        'iid': iid,
        'Timestamp': datetime.datetime.now(),
        'Date': parse(str(log_data[0])).date(),
        'Time': log_data[1],
        'DeviceName': log_data[2],
        'LogType': log_data[3],
        'IPVer': log_data[4],
        'Protocol': log_data[5],
        'SourceIP': log_data[6],
        'DestinationIP': log_data[7],
        'SourcePort': log_data[8],
        'DestinationPort': log_data[9],
        'SourceNatIP': log_data[10],
        'SourceNatPort': log_data[11],
        'BeginTime': log_data[12],
        'EndTime': log_data[13],
        'SendPkts': log_data[14],
        'SendBytes': log_data[15],
        'RcvPkts': log_data[16],
        'RcvBytes': log_data[17],
        'SourceVpnID': log_data[18],
        'DestinationVpnID': log_data[19],
        'PolicyName': log_data[20],
        'Data': str(log_data[21]),
        'Hash': log_data[22],
        'qsize': qsize
    }
    try:
        es.index(index=index, doc_type="session_teardown", body=doc)
    # except elasticsearch.exceptions.ConflictError as ex:
    #     es.delete(index=index, doc_type="session_teardown", id=iid)
    #     es.create(index=index, doc_type="session_teardown", id=iid, body=doc)
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
