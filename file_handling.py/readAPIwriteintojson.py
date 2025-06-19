import requests, json
api_url='https://jsonplaceholder.typicode.com/users'
data=requests.get(api_url)
users=data.json()

fp=open('newusers.jason','w')
json.dump(users,fp)
print("new file created")
fp.close()

