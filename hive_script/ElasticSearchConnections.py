import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import os

es = Elasticsearch(['http://macquarie-dev-es-data-0.dev.digitalreasoning.com:9200'],timeout=600)
es.indices.create(index = 'helloworld',body={})

print('Hello Elasticsearch')

liste_hello = ['hello1', 'hello2']
liste_world = ['world1', 'world2']
df = pd.DataFrame(data={'hello': liste_hello, 'world': liste_world})

# Bulk inserting documents. Each row in the DataFrame will be a document in ElasticSearch
documents = df.to_dict(orient='records')
bulk(es, documents, index='helloworld', doc_type='foo', raise_on_error=True)