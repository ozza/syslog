import datetime
import elasticsearch
from dateutil.parser import parse


def um_db_writer(es, index, log_data, iid, qsize):
    if len(log_data) == 15:
        doc = {
            'iid': iid,
            'Timestamp': datetime.datetime.now(),
            'Date': parse(str(log_data[0])).date(),
            'Time_FW': log_data[1],
            'DeviceName': log_data[2],
            'LogType': log_data[3],
            'UserName': log_data[4],
            'Vsys': log_data[5],
            'SourceIP': log_data[6],
            'SourceMAC': log_data[7],
            'LogonTime': log_data[8],
            'LogonMode': log_data[9],
            'AuthenticationMode': log_data[10],
            'DeviceCategory': log_data[11],
            'ParentGroup': log_data[12],
            'Data': str(log_data[13]),
            'Hash': log_data[14],
            'qsize': qsize
        }
        try:
            es.index(index=index, doc_type="um", body=doc)
        # except elasticsearch.exceptions.ConflictError as ex:
        #     es.delete(index=index, doc_type="um", id=iid)
        #     es.create(index=index, doc_type="um", id=iid, body=doc)
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

    elif len(log_data) == 16:
        doc = {
            'iid': iid,
            'Timestamp': datetime.datetime.now(),
            'Date': parse(str(log_data[0])).date(),
            'Time_FW': log_data[1],
            'DeviceName': log_data[2],
            'LogType': log_data[3],
            'UserName': log_data[4],
            'Vsys': log_data[5],
            'SourceIP': log_data[6],
            'ParentGroup': log_data[7],
            'LogonTime': log_data[8],
            'LogoutTime': log_data[9],
            'ObversePackets': log_data[10],
            'ObverseBytes': log_data[11],
            'ReversePackets': log_data[12],
            'ReverseBytes': log_data[13],
            'Data': str(log_data[14]),
            'Hash': log_data[15],
            'qsize': qsize
        }
        try:
            es.index(index=index, doc_type="um", body=doc)
        # except elasticsearch.exceptions.ConflictError as ex:
        #     es.delete(index=index, doc_type="um", id=iid)
        #     es.create(index=index, doc_type="um", id=iid, body=doc)
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
