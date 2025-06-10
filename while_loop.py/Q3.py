# list objects using for and while iterations 
eids=[101,102,103,104,105]
print(eids)
print(eids [0])
print(eids [1])
print(eids [2])
print(eids [3])
print(eids [4])
#print(eids [5]) #out of range error
print('using for loop')
i=0
for eid in eids:
    print(eids[i])
    i=i+1
print('using while loop')
i=0
while i<=3:
    print(eids[i])
    i=i+1