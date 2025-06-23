#file not found error

#error handling done through try,except,finally,raise

fp=None

try:
    fp=open('emp.txt','r')
except FileNotFoundError as errr:
    fp=open('defalut.txt','r')

data=fp.read()
print(data)
print("gm")
