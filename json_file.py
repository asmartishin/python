import json

def fileJsonDump(filename, json_data):
    with open(filename, 'w') as dump_file:
        json.dump(json_data, dump_file)

def fileJsonLoad(filename):
    with open(filename) as read_file:
        json_data = json.load(read_file)
    return json_data
