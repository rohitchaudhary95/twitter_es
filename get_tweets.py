from twitter import Api
from elasticsearch import Elasticsearch
from elasticsearch import helpers

ELASTICSEARCH_HOST = "localhost"
ELASTICSEARCH_PORT = 9200
ELASTICSEARCH_INDEX_NAME = "final_fifa_tweets"


CONSUMER_KEY = 'p5We1f9LZ1w10cV6qaoks84Cs'
CONSUMER_SECRET = 'jZlh70JRQPkhk0onuj2DavUhHGMVm0MwaJJ1gpLJKMVjBKz0ch'
ACCESS_TOKEN = '124730597-h0QwfCK1uJ1xsC1KDDzaf58Lk661t4CyNbx9YqKK'
ACCESS_TOKEN_SECRET = 'kLiqSETGh6gU0VErd5eRHw03fy4wl8vy43Bqlum1aMKVo'

api = Api(CONSUMER_KEY,
          CONSUMER_SECRET,
          ACCESS_TOKEN,
          ACCESS_TOKEN_SECRET)

es = Elasticsearch([{'host': ELASTICSEARCH_HOST, 'port': ELASTICSEARCH_PORT}])


if not es.indices.exists(ELASTICSEARCH_INDEX_NAME):
	request_body = {
		    "mappings": {
		        "data": {
		            "properties": {
		                "tweet": {
		                    "type": "object"
		                },
                        "sentiment": {
                            "type": "keyword"
                        },
                        "created_at": {
                            "type" : "date",
                            "format" : "EEE MMM dd HH:mm:ss Z YYYY"
                        }
		            }
		        }
		    }
		}
	res = es.indices.create(index = ELASTICSEARCH_INDEX_NAME, body = request_body)
	print(" response: '%s'" % (res))

from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(text)
    maxx=-1
    for s in ss.keys():
        if(ss[s]>maxx):
            maxx = ss[s]
            max_type = s
    return str(max_type)

def get_tweets():
    results = api.GetSearch(raw_query="q=fifa&lang=en&count=100")
    actions = []
    for r in results:
        x = r.AsDict()
        action = {
            "_index": ELASTICSEARCH_INDEX_NAME,
            "_type": "data",
            "_source": {
                'tweet': x,
                'sentiment': str(get_sentiment(x['text'])),
                'created_at': x['created_at']
            }
        }
        actions.append(action)

    if len(actions) > 0:
        helpers.bulk(es, actions)

get_tweets()
#get_sentiment("today is a bad day")
