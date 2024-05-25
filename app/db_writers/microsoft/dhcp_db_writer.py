import datetime
import elasticsearch


def dhcp_db_writer(es, index, log_data, iid, qsize):
    doc = {
        'iid': iid,
        'Timestamp': datetime.datetime.now(),
        'Date': log_data[1],
        'Time': log_data[2],
        'EventId': log_data[0],
        'EventName': log_data[3],
        'ClientIp': log_data[4],
        'HostName': log_data[5],
        'MacAddress': log_data[6],
        'UserName': log_data[7],
        'TransactionId': log_data[8],
        'Data': str(log_data[9]),
        'Hash': log_data[10],
        'qsize': qsize
    }
    try:
        es.index(index=index, doc_type="dhcp", body=doc)
    # except elasticsearch.exceptions.ConflictError as ex:
    #     es.delete(index=index, doc_type="dhcp", id=iid)
    #     es.create(index=index, doc_type="dhcp", id=iid, body=doc)
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
