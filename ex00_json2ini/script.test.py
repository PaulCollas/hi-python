######## TXT TO JSON #######
# import json

# # file selected
# filename = 'data.ini'

# # text will be stored
# dict1 = {}

# # creating dictionnary
# with open(filename) as fh : 

#     for line in fh:

#         # reads each lines
#         command, description = line.strip().split(None, 3)

#         dict1[command] = description.strip()

# # creating the json file
# out_file = open("file.json", "w")

# json.dump(dict1, out_file, indent = 4, sort_keys = False)

# out_file.close()




######## JSON TO INI ###########

# import json

# from configparser import ConfigParser
# config = ConfigParser()

# filename = 'config.ini'
# # config.read('config.ini')


# dict1 = {}

# with open(filename) as f:

#     for line in f: 
#         command, description = line.strip().split(None, 3)

#     out_file = open("file.json", "w")

#     json.dump(dict1, out_file, indent = 4, sort_keys = False)
#     config.write(f)

#     out_file.close()


#################### INI TO JSON #################

## Create INI File

# from configparser import ConfigParser
# config = ConfigParser()

# config.read('config.ini')
# config.add_section('people')
# config.set('people', 'name', 'paul collas')
# config.set('people', 'age', '20 ans')
# config.set('people', 'ecole', 'efrei')

# with open('config.ini', 'w') as f:
#     config.write(f)

# ## Export to Json

# import json

# ## Write inside the json file
# config = {"name": "paul collas", "age": "20 ans", "ecole": "efrei"}

# # with open('file.json', 'w') as f:
# #     json.dump(config, f)

# ## Read data from ini file

# with open('file.json', 'r') as f:
#     config = json.load(f)