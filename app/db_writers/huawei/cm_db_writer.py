import datetime
import elasticsearch
from dateutil.parser import parse


def cm_db_writer(es, index, log_data, iid, qsize):
    if len(log_data) == 27:
        doc = {
            'iid': iid,
            'Timestamp': datetime.datetime.now(),
            'Date': parse(str(log_data[0])).date(),
            'Time_FW': log_data[1],
            'DeviceName': log_data[2],
            'LogType': log_data[3],
            'ACMAC': log_data[4],
            'ACNAME': log_data[5],
            'APMAC': log_data[6],
            'APNAME': log_data[7],
            'SSID': log_data[8],
            'RADIOID': log_data[9],
            'USER': log_data[10],
            'MAC': log_data[11],
            'IPADDRESS': log_data[12],
            'TIME': log_data[13],
            'ZONE': log_data[14],
            'DAYLIGHT': log_data[15],
            'SESSIONTIME': log_data[16],
            'ERRCODE': log_data[17],
            'RESULT': log_data[18],
            'USERGROUP': log_data[19],
            'AUTHENPLACE': log_data[20],
            'EXTENDINFO': log_data[21],
            'CIBID': log_data[22],
            'INTERFACE': log_data[23],
            'ACCESSTYPE': log_data[24],
            'Data': str(log_data[25]),
            'Hash': log_data[26],
            'qsize': qsize
        }
        try:
            es.index(index=index, doc_type="cm", body=doc)
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

    elif len(log_data) == 24:
        doc = {
            'iid': iid,
            'Timestamp': datetime.datetime.now(),
            'Date': parse(str(log_data[0])).date(),
            'Time_FW': log_data[1],
            'DeviceName': log_data[2],
            'LogType': log_data[3],
            'ACMAC': log_data[4],
            'ACNAME': log_data[5],
            'APMAC': log_data[6],
            'APNAME': log_data[7],
            'SSID': log_data[8],
            'RADIOID': log_data[9],
            'USER': log_data[10],
            'MAC': log_data[11],
            'IPADDRESS': log_data[12],
            'TIME': log_data[13],
            'ZONE': log_data[14],
            'DAYLIGHT': log_data[15],
            'ERRCODE': log_data[16],
            'RESULT': log_data[17],
            'USERGROUP': log_data[18],
            'CIBID': log_data[19],
            'INTERFACE': log_data[20],
            'ACCESSTYPE': log_data[21],
            'Data': str(log_data[22]),
            'Hash': log_data[23],
            'qsize': qsize
        }
        try:
            es.index(index=index, doc_type="cm", body=doc)
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

    elif len(log_data) == 25:
        doc = {
            'iid': iid,
            'Timestamp': datetime.datetime.now(),
            'Date': parse(str(log_data[0])).date(),
            'Time_FW': log_data[1],
            'DeviceName': log_data[2],
            'LogType': log_data[3],
            'ACMAC': log_data[4],
            'ACNAME': log_data[5],
            'APMAC': log_data[6],
            'APNAME': log_data[7],
            'SSID': log_data[8],
            'RADIOID': log_data[9],
            'USER': log_data[10],
            'MAC': log_data[11],
            'IPADDRESS': log_data[12],
            'TIME': log_data[13],
            'ZONE': log_data[14],
            'DAYLIGHT': log_data[15],
            'ERRCODE': log_data[16],
            'RESULT': log_data[17],
            'USERGROUP': log_data[18],
            'AUTHENPLACE': log_data[19],
            'CIBID': log_data[20],
            'INTERFACE': log_data[21],
            'ACCESSTYPE': log_data[22],
            'Data': str(log_data[23]),
            'Hash': log_data[24],
            'qsize': qsize
        }
        try:
            es.index(index=index, doc_type="cm", body=doc)
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
