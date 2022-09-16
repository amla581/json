import csv

with open("details.csv","w") as obj:
    fobj=csv.writer(obj)
    fobj.writerow(["roll","name","total"])
    while True:
        roll=int(input("enter the roll"))
        name=input("enter the name")
        total=int(input("enter the total"))
        record=[roll,name,total]
        fobj.writerow(record)
        ch=int(input("1==enter more \n 2==exit \n enter your choice"))
        if ch==2:
            break 
with open("details.csv","r") as obj:
    fobj=csv.reader(obj)
    for i in fobj:
        print(i)

