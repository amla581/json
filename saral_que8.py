a=["neelam","programer","24","2400"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]

e=["name","designation","age","salary"]

d1={}
d2={}
d3={}
d4={}

dic={}

i=0
while(i<len(a)):
    j=0
    while(j<len(e)):
        d1[e[j]]=a[j]
        d2[e[j]]=b[j]
        d3[e[j]]=c[j]
        d4[e[j]]=d[j]
        j=j+1
    dic["emp1"]=d1
    dic["emp2"]=d2
    dic["emp3"]=d3
    dic["emp4"]=d4
    i=i+1
# print(dic)

import json
# filedata=json.dumps(dic,indent=4)

outfile=open("saral_que8.json","w")
filedata=json.dump(dic,outfile,indent=4)

# print(filedata)
outfile.close()
