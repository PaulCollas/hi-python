########### JSON TO INI FILE ###############

import json

# OPEN JSON FILE
file = open('file.json', 'r')

# LOAD INFORMATION IN JSON FILE
data = json.load(file)
file.close()


with open(r'file.json') as file:
    data = json.load(file)

# SET ALL KEYS & ITEMS IN JSON FILE
data.keys()
data.items()

string = ""

# CONDITION IF SET KEY IN JSON FIILE
for key in data.keys():

    # SET STRING WITH KEYS
    string = string + "[" + key + "]\n"

    # SET STRING WITH SUB_KEYS
    for sub_key in data[key].keys():
        string = string + sub_key + "=" + data[key][sub_key] + "\n"
    string = string + "\n"

# PRINT THE RESPONSE
print(string)

# OPEN INI FILE
with open('config.ini', 'w') as file:

    # WRITE INSIDE INI FILE
    file.write(string)

