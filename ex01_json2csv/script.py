
###### TEST 1 ######
# import pandas as pd
# import json

# filename = 'data.json'

# info = json.loads(filename)

# df = pd.json_normalize(info['Eleves'])

# df.to_csv("file.csv")



###### TEST 2 ######
# import pandas as pd

# df = pd.read_json('export.json')
# print(df)

# df.to_csv()


###### TEST 3 with no pandas ########

# import json
# import csv

# f = open('data.json')
# data = json.load(f)
# print(data)
# f.close()

# f = open('file.csv')
# csv_file = csv.writer(f)
# for item in data:
#     f.writerow(item)

# f.close()


###### TEST 4 ###########

import json
import csv

with open('data.json') as fichier_json:
    data = json.load(fichier_json)
 
cities = data['city']

toCsv = open('file.csv', 'w')

csv_writer = csv.writer(toCsv)

count = 0
 
for ct in cities:
    if count == 0:

        header = ct.keys()
        csv_writer.writerow(header)
        count += 1
        
    csv_writer.writerow(ct.values())
 
toCsv.close()