from elasticsearch import helpers, Elasticsearch
es = Elasticsearch(['some-elastic-url'],timeout=600)


mymapping={"mappings": {"geotest":{"properties":{"location":{"type":"geo_point","lat_lon":"True","geohash":"True"}}}}}


#es.indices.delete(index = 'geotest')
es.indices.create(index = 'geotest', body = mymapping)
