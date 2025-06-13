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

