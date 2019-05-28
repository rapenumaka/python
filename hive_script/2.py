from pyhive import hive
import json
import numpy as np
import pandas as pd
import dateutil.parser
from elasticsearch import helpers, Elasticsearch
from collections import namedtuple
from elasticsearch.helpers import bulk

host_name = "macquarie-dev-nn.dev.digitalreasoning.com"
port = 10001
username = "synthesys"

response =[]
newresult =[]





def hiveconnections(host_name,port,username):
    conn = hive.Connection(host=host_name,
                           port = port,
                           username = username)
    cursor = conn.cursor()
    ##cursor.execute("SHOW DATABASES")
    cursor.execute("use hrdata")
    #cursor.execute("select website_logs_view_device_dst_hostname,website_logs_view_user_src_risk_level,website_logs_view_web_policy,website_logs_view_web_category from hr_mock_data_weblogs_macquarie limit 10")
    cursor.execute("select * from HR_MOCK_DATA_ACCESSLOGS_WITH_EVENTS_JSON_MACQUARIE limit 9900")
    response = cursor.fetchall()
    eventsList = []
    gate =[]
    eventDates = []
    emp_nos = []
    timestamp = []
    date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    for r in response:
        for x in r:
            first = x[16:]
            data = first[:-1]
            loaded_json = json.loads(data)

            gate.append(loaded_json["LOGDEVDESCRP"])
            eventDates.append(loaded_json["EVNT_DAT"])
            emp_nos.append(loaded_json["MG_EMPLOYEE_NUMBER"])
            d = dateutil.parser.parse(loaded_json["EVNT_DAT"])
            timestamp.append(d.strptime(loaded_json["EVNT_DAT"],date_format))

            newresult.append(loaded_json)
    gate_asarray = np.asarray(gate)
    eventDates_asarray = np.asarray(eventDates)
    emp_nos_asarray = np.asarray(emp_nos)
    time_diff = np.asarray(timestamp)
    dataFrame =  pd.DataFrame({ 'MGL_EMP' :emp_nos_asarray,
        'GATE':gate_asarray,'TIMESTAMP' :eventDates_asarray,
        'TIME' : time_diff
    })

    desired_width = 320
    pd.set_option('display.width', desired_width)

    pd.set_option('display.max_columns', 10)

    print(dataFrame)
    print('**************************************')
    print('\n')
    print('\n')

    ids = dataFrame['MGL_EMP']

    d1 = dataFrame[ids.isin(ids[ids.duplicated()])].sort_values(by= 'TIME')
    ##print(d1.index['MGL_EMP = "E-4-3-91-915972808-5070907760-123101"'])
    return d1











df = hiveconnections(host_name,port,username)

print(df)

#df['delta'] = (df['TIME']-df['TIME'].shift()).fillna(0)


#df['delta'] = (df['TIME'] - df['TIME'].shift()).fillna(0)

#df['Seconds_Apart'] = df['delta'].apply(lambda x: x / np.timedelta64(1, 's')).astype('int64') % (24 * 60 * 60)



#df['delta'] = (df['TIME']-df['TIME'].shift()).fillna(0)
df['delta'] = (df['TIME']-df['TIME'].shift()).fillna(0)

df['Seconds_Apart'] = df['delta'].apply(lambda x: x  / np.timedelta64(1,'s')).astype('int64') % (24*60*60)
desired_width=320
pd.set_option('display.width', desired_width)


pd.set_option('display.max_columns',10)





newDataframe = df[df['Seconds_Apart' ] < 30]

print(newDataframe[1:])



es = Elasticsearch(['http://macquarie-dev-es-data-0.dev.digitalreasoning.com:9200'],timeout=600)

es.indices.delete(index= 'accesslogs_test1')
es.indices.create(index= 'accesslogs_test1', body = {})
documents = newDataframe.to_dict(orient='records')
bulk(es,documents, index='accesslogs_test1',doc_type='mock')



