# -*- coding: utf-8 -*-
from django.conf import settings
from elasticsearch import Elasticsearch


#
# Elasticsearch utils
#


def get_elasticsearch_client() -> Elasticsearch:
    return Elasticsearch(**settings.ELASTICSEARCH_CONFIG)


def index_document(
    document: dict, es_client: Elasticsearch = None, index: str = "meta-dados-rio"
) -> dict:
    """
    Index a document in Elasticsearch.
    """
    es_client = es_client or get_elasticsearch_client()
    return es_client.index(index=index, document=document)
