def get_latest_id(es, index, packet_type, irange):
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
                            "match_all": {}
                        },
                        "filter": {
                            "range": {
                                "Timestamp": {"gt": "now-"+irange}
                            }
                        }
                    }
                }
            })

            return response['hits']['hits'][0]['_source']['iid']+1
        else:
            return 0
    except Exception as ex:
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
                            "match_all": {}
                        }
                    }
                }
            })

            return response['hits']['hits'][0]['_source']['iid'] + 1
        else:
            return 0
