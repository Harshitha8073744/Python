# set object: group of elements as one entity
#group of unique elelments
#duplicate elements are not allowed
#indexing concept is not applicable, insertion order not maintained

#to create empty set we have to use set function because s={} will become dict object
s1=set()
print(type(s1))
s2={10}
print(type(s2))
s3={}
print(type(s3))
s4={10,20,10,30,40,50,50,50}
print(s4)

#updating
s4.add('gg')
print(s4)

s4.remove('gg')
print(s4)