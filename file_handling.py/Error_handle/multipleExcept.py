#only one error handling at a time i.e if zero error occurs it terminates there only file not found error will not be there
fp=None
try:
    num= int(input("enter number"))
    print(num)
    print(num/1)
    fp=open("emp23.txt",'r')
except ValueError as err:
    print("please enter digits only")

except ZeroDivisionError as err:
    print("can't divide by zero")

except FileNotFoundError as err:
    print("chrck if file exisits")

except:
    print("parent exception")