from elasticsearch import Elasticsearch
from constants import ELASTICSEARCH_PORT, ELASTICSEARCH_HOST

es = Elasticsearch([{'host': ELASTICSEARCH_HOST, 'port': ELASTICSEARCH_PORT}])
