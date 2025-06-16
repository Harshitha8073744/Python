# Inbuilt function executing provided function for every element of the sequence
# map(addone,product prices)

def addone(price):
    return price+1

product_prices=[98,198,298,398,498]

new=map(addone,product_prices)
new_prices=list(new)
print(new_prices)

# with lambda

new1=map(lambda price:price+1,product_prices)
new_prices=list(new1)
print(new_prices)

#singlr line code

