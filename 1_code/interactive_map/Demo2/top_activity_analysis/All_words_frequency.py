from bson.son import SON
from pymongo import Connection
import json
from collections import Counter
from prettytable import PrettyTable

conn = Connection()
db = conn.DB2

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
			
pt = PrettyTable(field_names=['Words', 'frequency'])

for i in  [words]:   
	c = Counter(i)
	[pt.add_row(kv) for kv in c.most_common()[:300]]

pt.align['Words'], pt.align['frequency'] = 'l', 'r'
print pt