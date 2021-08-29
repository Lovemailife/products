#記帳程式
products=[]
while True:
    name =input('商品名:')
    if name == 'q':
        break
    price = input('價錢:')
    p = [name, price]
    products.append(p)
print(products)    

print(products[0][0])