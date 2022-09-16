# python to json
import json
num={'name': 'David','class':'I','age': 6}
p=json.dumps(num,indent=3)
print(p)