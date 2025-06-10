# group of key value pairs as an entity 
#duplicate keys are not allowed
# indexing is not possible

d1={}
emp={ 'eid':101,
        'ename':'rahul',
        'esal':45000.45,
        'loc':['wy','nd','noida']}

print(emp['eid'])
print(emp['ename'])
print(emp['esal'])
print(emp['loc'][1])

#methods

# print(emp['email'])# key error

print(emp.keys()) # print all keys can be done using for loop also

print(emp.values()) # printing the values

print(emp.items())# key and value

'''for value in emp.values():
    print(value)'''

print(emp.get('eid')) # same os print(emp['eid])
print(emp.get('ename'))



