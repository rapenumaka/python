from pyhive import hive
import json
import numpy as np
import pandas as pd
import dateutil.parser

df = pd.DataFrame({'Animal' : ['Falcon', 'Falcon',
                              'Parrot', 'Parrot'],
                    'Max Speed' : [380., 370., 24., 26.]})

df1 = pd.DataFrame([['A','C','A','B','C','A','B','B','A','A'], ['ONE','TWO','ONE','ONE','ONE','TWO','ONE','TWO','ONE','THREE']]).T
df1.columns = [['Alphabet','Words']]
df1['COUNTER'] =1       #initially, set that counter to 1.
group_data = df1.groupby(['Alphabet','Words'])['COUNTER'].sum() #sum function
print(df1)

print(df)

print(df.groupby(by='Animal'))
