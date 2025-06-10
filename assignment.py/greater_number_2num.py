#Write a program to find the biggest of given 2 numbers from the command prompt
i=int(input("please enter the first number"))
j=int(input("please enter the second number"))
if i>j:
    print(i,"is greater than",j)
if j>i:
    print(j,"is greater than",i)
if i==j:
    print("they are equal")
