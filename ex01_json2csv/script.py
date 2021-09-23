###### JSON TON CSV ###########

import json
import csv

# OPEN JSON FILE
with open('data.json') as fichier_json:
    data = json.load(fichier_json)
 
# KEY FROM DATA IN JSON
cities = data['city']

# OPEN CSV FILE
toCsv = open('file.csv', 'w')

# PREPARE CSV FILE TO WRITE
csv_writer = csv.writer(toCsv)

count = 0
 
for ct in cities:
    if count == 0:

        # SELECTED KEYS IN HEADER
        header = ct.keys()

        # WRITE KEY IN HEADER
        csv_writer.writerow(header)
        count += 1
    
    # WRITE VALUES OF KEYS
    csv_writer.writerow(ct.values())
 
toCsv.close()