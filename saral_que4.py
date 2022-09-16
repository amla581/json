sort={'4': 5, '6': 7, '1': 3, '2': 4}
c=[]
for p in sort:
    g=sort[p]
    c.append(g)
    s=sorted(c)

b=[]
for i in sort:
    a=i
    b.append(a)
    d=sorted(b)
    
new_dict={}
j=0
while j<len(b):
    new_dict[b[j]]=s[j]
    j+=1
dic=new_dict
print(dic)
import json
j={'1':3,'2':4,'4':5,'6':7}
p=json.dumps(j,indent=2)
print(p)



