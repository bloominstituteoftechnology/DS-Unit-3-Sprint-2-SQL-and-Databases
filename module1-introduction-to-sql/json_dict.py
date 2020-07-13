import json 
with open('testdata.json') as json_file:
    data = json.loads(json_file)
    print(data[1]['model'])
