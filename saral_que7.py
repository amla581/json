# python tojson
import json
dict1={}
file=open("filedata.txt","r")
for i in file:
    key, value = i.strip().split(None, 1)
    dict1[key]=value.strip()
outfile=open("filedata.json","w")
json.dump(dict1,outfile,indent=3)
print(json.dumps(dict1,indent=3))
outfile.close()
