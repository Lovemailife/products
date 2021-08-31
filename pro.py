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

print(products[0][0]) #大清單中第一個清單的第一個位置

for p in products:
    #print(p)
    print(p[0],'的價格是',p[1], '元')

with open ('products.csv', 'w', encoding='utf-8') as f :
    f.write('商品, 價格\n')
    for p in products:
        f.write(p[0]+','+p[1]+'\n')