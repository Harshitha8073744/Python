#segregate odd/even number into new list
num=[37,18,31,14,8,12,7]
even=[]
odd=[]
'''for n in num:
    if num%2==0:
        even.append(n)
    else:
        odd.append(n)'''

print(even,odd)

def check_even(num):
    return num%2==0

even=list(filter(check_even,num))

print(even)

even=list(filter(lambda num:num%2==0,num))
print(even)


