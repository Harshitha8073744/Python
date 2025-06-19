import json
fp1=open("emp.json",'r')
employees=json.load(fp1)

print(type(employees))

for emp in employees:
    print(emp['ename'])

fp1.close()