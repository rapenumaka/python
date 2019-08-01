from pyhive import hive
import json
import numpy as np
import pandas as pd
import dateutil.parser
from elasticsearch import helpers, Elasticsearch
from elasticsearch.helpers import bulk
import argparse

host_name = 
port = 10001
username = 
elastic_url = 
elastic_schema =






def consoleSetup():
    desired_width = 320
    np.set_printoptions(linewidth=desired_width)
    pd.set_option('display.width', desired_width)
    pd.set_option('display.max_columns', 10)
    pd.options.mode.chained_assignment = None



def hiveconnections(host_name,port,username):
    try:
        response = []
        newresult = []
        conn = hive.Connection(host=host_name,
                           port = port,
                           username = username)
        cursor = conn.cursor()
        cursor.execute("use hrdata")
        cursor.execute("select website_logs_event_raw from HR_MOCK_DATA_ACCESSLOGS_WITH_EVENTS_JSON_MACQUARIE")
        response = cursor.fetchall()
    except :
        print('Problem connecting to Hive Table')
    gate =[]
    eventDates = []
    emp_nos = []
    timestamp = []
    directions = []
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
            directions.append(((loaded_json["LOGDEVDESCRP"])[18:]).strip())

            newresult.append(loaded_json)
    gate_asarray = np.asarray(gate)
    eventDates_asarray = np.asarray(eventDates)
    emp_nos_asarray = np.asarray(emp_nos)
    time_diff = np.asarray(timestamp)
    direction = np.asarray(directions)
    dataFrame =  pd.DataFrame({ 'MGL_EMP' :emp_nos_asarray,
        'GATE':gate_asarray,'TIMESTAMP' :eventDates_asarray,
        'TIME' : time_diff,
        'DIRECTION':direction

    })
    d1 = dataFrame.sort_values(by = ['MGL_EMP','GATE'])
    return d1


def manual(df):

    df['MGL_EMP2'] = df['MGL_EMP'].shift(1)
    df['GATE_2'] = df['GATE'].shift(1)
    df['TIME_2'] = df['TIME'].shift(1)
    df['Equal'] = (df['MGL_EMP2'] == df['MGL_EMP'])
    df['Equal_2'] = (df['GATE'] == df['GATE_2'])
    df = df[df['Equal']]
    df = df[df['Equal_2']]
    df['delta'] = df['TIME'] - df['TIME_2']
    #df['TIME_DIFFERENCE'] = df['delta'].apply(lambda x: x / np.timedelta64(1, 's')).astype('int64') % (24 * 60 * 60)
    df['TIME_DIFFERENCE'] = df['delta'].dt.total_seconds()
    print(df)
    newDataframe = df[df['TIME_DIFFERENCE'] < 30]

    print('\n')
    return newDataframe


def addGateFrame(newDataframe):
    gateFrame = {"L29 Main Entrance D1": "OutIn",
                 "L29 Main Entrance D2": "InOut",
                 "L29 Side Entrance D1": "OutIn",
                 "L29 Side Entrance D2": "InOut",
                 "L30 Main Entrance D1": "OutIn",
                 "L30 Main Entrance D2": "InOut",
                 "L29 Green Lab D3": "InIn",
                 "L29 Green Lab D4": "InIn"}
    newDataframe['DIRECTION'].replace(gateFrame, inplace=True)

    del newDataframe['MGL_EMP2']
    del newDataframe['GATE_2']
    del newDataframe['TIME_2']
    del newDataframe['Equal']
    del newDataframe['Equal_2']
    del newDataframe['TIME']
    del newDataframe['delta']

    newDataframe.astype(str)

    print(newDataframe)
    return newDataframe


def loadToES(dataframe,elastic_url,elastic_index):
    try:
        es = Elasticsearch(elastic_url, timeout=600)
        es.indices.create(index= elastic_index, body = {})
        documents = dataframe.to_dict(orient='records')
        bulk(es, documents, index=elastic_index, doc_type='mock')
    except:
        print('Index already exists.. Indexing to the existing one ...')


def checkArguments(string):
    if not string:
        raise Exception('usage: Accesslogs.py [-h] [-hive_host HIVE_HOST] [-hive_port HIVE_PORT]'
                     '[-hive_usr HIVE_USR] [-elastic_url ELASTIC_URL]'
                     '[-elastic_index ELASTIC_INDEX]')

def main():

    parser = argparse.ArgumentParser(
        description="This is script"
    )
    parser.add_argument('-hive_host', action="store")
    parser.add_argument('-hive_port', action="store", type=int)
    parser.add_argument('-hive_usr', action="store")
    parser.add_argument('-elastic_url', action="store")
    parser.add_argument('-elastic_index', action="store")



    consoleSetup()
    print(parser.parse_args())
    args=parser.parse_args()
    df = hiveconnections(args.hive_host,args.hive_port,args.hive_usr)
    newDataframe= manual(df)
    df1 = addGateFrame(newDataframe)
    loadToES(df1,args.elastic_url,args.elastic_index)




if __name__ == '__main__':
      main()















