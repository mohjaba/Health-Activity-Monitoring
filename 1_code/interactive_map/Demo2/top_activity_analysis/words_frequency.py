from bson.son import SON
from pymongo import Connection
import json
from collections import Counter
from prettytable import PrettyTable

conn = Connection()
db = conn.DB2

total=['run','running','swimming','gym','ran','biked','football','fitness','bike','weight','yoga','jogger','training',' runner','biking','golf','basketball','hockey','tennis','baseball','crossfit','pullups','diet','cycling']

coords = db.coll2.find({"coordinates":{"$type":3}})

text = [data1['text'] for data1 in coords]

text = [s.replace('#','') for s in text]
text = [s.replace('.','') for s in text]
text = [s.replace('!','') for s in text]
text = [s.replace('@','') for s in text]
text = [s.replace(':','') for s in text]
text = [s.replace(',','') for s in text]
text = [s.replace('-','') for s in text]
text = [s.replace('?','') for s in text]


words = [ w for t in text 
			for w in t.lower().split()]
			
pt = PrettyTable(field_names=['Top Activites', 'frequency'])
c = Counter(words)

[pt.add_row((s, c[s])) for s in total[:10]]
data = [(s,c[s]) for s in total[:10]]

data = sorted(data, key = lambda x: (x[1]),reverse=True)

pt.align['Top Activites'], pt.align['frequency'] = 'l', 'r'

print pt.get_string(sortby="frequency", reversesort=True)