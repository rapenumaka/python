import json

print('Hello JsonLoad ')

json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'

json_baba ='{"TSTAMP":873347487,"EVNT_DAT":"2018-02-09T17:47:49.000Z","LOGDEVDESCRP":"H1PMAEC029RE040101 L29 Main Entrance D1","MG_DIVISION":"Security Control Group","LNAME":"jamie","Normalised":true,"MG_EMPLOYEE_NUMBER":"E-6-8-19-858049633-6062936857-734874","event_ts":"2018-02-09T9:47:49.000Z","MG_SHORTNAME":"NOBC","CARDNO":"90497","491329991":307818152,"ORIG_TIME":"2018-02-09T17:47:49.000Z","type_id":"Prowatch:Access","EVNT_DESCRP":"Local Grant","FNAME":"jennings","REC_DAT":"2018-02-09T17:47:49.000Z","COMP_NAME":"H1PMAEC Contractor","MG_LOCATION":"Sydney Office","SOME_GROUP":"Security Control Group"}'

print(json.loads(json_baba))


loaded_json = json.loads(json_baba)
for x in loaded_json:
	print("%s: %s" % (x, loaded_json[x]))
