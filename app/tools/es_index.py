#!/usr/bin/python3.6

from elasticsearch import *
import configparser
import json

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("../../config.ini")

    mappingsFile = "mappings.json"
    mappingsContent = open(mappingsFile).read()

    es = Elasticsearch(
        [config["ELASTICSEARCH"]["Host"]],
        timeout=30,
        maxsize=int(1),
        retry_on_timeout=True,
        max_retries=100,
    )

    es.indices.create(index="index", body=mappingsContent)
