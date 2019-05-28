import dateutil.parser
import pandas as pd
D = "yyyy-MM-ddTHH:mm:sssZ"
M = "2018-02-09T22:00:00.000Z"
date_format = "%Y-%m-%dT%H:%M:%S.%fZ"

d = dateutil.parser.parse(M)
print(d.strptime(M,date_format))
print(type(d))

print(d.strftime('%H:%M:%S'))
print(pd.to_datetime(M))


v1 = "H1PMAEC029RE040102 L29 Main Entrance D2"
print(v1[18:].strip())


