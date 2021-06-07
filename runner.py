import json

filehandle = open('properties.json')

json_load = json.load(filehandle)

for object in json_load:
    print("\n==================\n",object)
    
print(json_load[object])
