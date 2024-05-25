def get_last_mac_of_an_ip_address(es, index, packet_type, irange, ip):
    try:
        count = es.search(index=index, doc_type=packet_type)
        if count['hits']['total'] > 0:
            response = es.search(index=index, doc_type=packet_type, body={
                "sort": [
                    {"iid": {"order": "desc"}}
                ],
                "size": 1,
                "query": {
                    "bool": {
                        "must": {
                            "match": {
                                "IpAddress": ip
                            }
                        },
                        "filter": {
                            "range": {
                                "Timestamp": {"gt": "now-" + irange}
                            }
                        }
                    }
                }
            })

            return response['hits']['hits'][0]['_source']['MacAddress']
        else:
            return 0
    except Exception as ex:
        return 0
