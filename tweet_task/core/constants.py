ELASTICSEARCH_HOST = "localhost"
ELASTICSEARCH_PORT = 9200
ELASTICSEARCH_INDEX_NAME = "final_fifa_tweets"
PAGE_SIZE=10

def match_query(term):
    query = {
        "query": {
            "match": {
                "_all": term
            }
        }
    }
    return query

def date_range_query(field, range_start, range_end):
    query = {
        "query": {
            "range": {
                field: {
                    "gte": range_start,
                    "lte": range_end,
                    "format": "dd/MM/yyyy"
                }
            }
        }
    }
    return query

def numeric_range_query(field, range_start, range_end):
    query = {
                "query": {
                    "range": {
                        field: {
                            "gte": range_start,
                            "lte": range_end,
                        }
                    }
                }
            }

    return query

def imp_query(query_type, field, field_value):
    query = {
        "query": {
            query_type: {
                field: field_value
            }
        }
    }
    return query

def senti_query(sentiment):
    query = {
        "query": {
            "term": {
                "sentiment": sentiment
            }
        }
    }
    return query