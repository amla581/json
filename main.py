import json

name={'a':'amla','b':'manvi','c':'suman','d':'kavita'}
with open("amla.json","w")as f:
    json.dump(name,f,indent=3)
    b=json.dumps(name,indent=4)
print(b)