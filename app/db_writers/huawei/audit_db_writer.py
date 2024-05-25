import datetime
import elasticsearch
from dateutil.parser import parse


def audit_db_writer(es, index, log_data, iid, qsize):
    if len(log_data) == 26:
        doc = {
            'iid': iid,
            'Timestamp': datetime.datetime.now(),
            'Date': parse(str(log_data[0])).date(),
            'Time': log_data[1],
            'DeviceName': log_data[2],
            'LogType': log_data[3],
            'SyslogId': log_data[4],
            'VSys': log_data[5],
            'AuditPolicy': log_data[6],
            'SrcIp': log_data[7],
            'DstIp': log_data[8],
            'SrcPort': log_data[9],
            'DstPort': log_data[10],
            'SrcZone': log_data[11],
            'DstZone': log_data[12],
            'User': log_data[13],
            'Protocol': log_data[14],
            'Application': log_data[15],
            'Profile': log_data[16],
            'AuditType': log_data[17],
            'EventNum': log_data[18],
            'Direction': log_data[19],
            'Command': log_data[20],
            'FileName': log_data[21],
            'FileSize': log_data[22],
            'Action': log_data[23],
            'Data': str(log_data[24]),
            'Hash': log_data[25],
            'qsize': qsize
        }

        try:
            es.index(index=index, doc_type="audit", body=doc)
        # except elasticsearch.exceptions.ConflictError as ex:
        #     es.delete(index=index, doc_type="audit")
        #     es.index(index=index, doc_type="audit", body=doc)
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

    else:
        doc = {
            'iid': iid,
            'Timestamp': datetime.datetime.now(),
            'Date': parse(str(log_data[0])).date(),
            'Time': log_data[1],
            'DeviceName': log_data[2],
            'LogType': log_data[3],
            'SyslogId': log_data[4],
            'VSys': log_data[5],
            'AuditPolicy': log_data[6],
            'SrcIp': log_data[7],
            'DstIp': log_data[8],
            'SrcPort': log_data[9],
            'DstPort': log_data[10],
            'SrcZone': log_data[11],
            'DstZone': log_data[12],
            'User': log_data[13],
            'Protocol': log_data[14],
            'Application': log_data[15],
            'Profile': log_data[16],
            'AuditType': log_data[17],
            'EventNum': log_data[18],
            'Direction': log_data[19],
            'URL': log_data[20],
            'Subject': log_data[21],
            'Content': log_data[22],
            'FileName': log_data[23],
            'FileSize': log_data[24],
            'URLCategory': log_data[25],
            'Data': str(log_data[26]),
            'Hash': log_data[27],
            'qsize': qsize
        }

        try:
            es.index(index=index, doc_type="audit", body=doc)
        # except elasticsearch.exceptions.ConflictError as ex:
        #     es.delete(index=index, doc_type="audit")
        #     es.index(index=index, doc_type="audit", body=doc)
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
