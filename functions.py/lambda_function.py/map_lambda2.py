<<<<<<< HEAD
#without lambda
enames=['rg','sg','nm','amith']
def changecase(names):
    return names.upper()


newnames=list(map(changecase,enames))
print(newnames)

#with lambda
print(list(map(lambda enames:enames.upper(),enames)))

#without map 
new_name=[]
for ename in enames:
    new_name.append(ename.upper())
print(new_name)

=======
#without lambda
enames=['rg','sg','nm','amith']
def changecase(names):
    return names.upper()


newnames=list(map(changecase,enames))
print(newnames)

#with lambda
print(list(map(lambda enames:enames.upper(),enames)))

#without map 
new_name=[]
for ename in enames:
    new_name.append(ename.upper())
print(new_name)

>>>>>>> 97f9261a9df0acc17e96c094d6bc43ad10a8b5c8
