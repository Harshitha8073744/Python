fp1=open('data.txt','r')
content=fp1.read()

fp2=open('xyz.txt','w')
content2=fp2.write(content)
fp1.close()
fp2.close()

print("new file created and read success")

