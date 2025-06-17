fp=open('logo.png','rb')
pic=fp.read()

fp1=open('create.png','wb')
fp1.write(pic)

print("new image created")
fp.close()
fp1.close()
