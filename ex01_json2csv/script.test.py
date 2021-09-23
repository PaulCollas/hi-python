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

