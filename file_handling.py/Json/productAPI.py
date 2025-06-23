'''import requests,json
API_url='https://dummyjson.com/products'
data=requests.get(API_url)#python type
print(type(data))

beauty=data.json()
print(type(beauty))

fp=open('beauty.json','w')
json.dump(beauty,fp)

print('new')
fp.close()'''

import requests,json
api_url='https://dummyjson.com/products'
data=requests.get(api_url)

product_data=data.json()

product=product_data['products']
print(type(product))
#transform data

beauty_products=[]
for prod in product:
    if prod['category']=='beauty':
        beauty_products.append(prod)

fp=open('beauty.json','w')

json.dump(beauty_products,fp)
print('new file')

fp.close()
