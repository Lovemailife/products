#讀取檔案
products=[]
with open ('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品,價格' in line:
            continue #跳過這回合
        name,price=line.strip().split(',') #split切割,遇到逗點就切割;strip去掉空格及換行符號
        products.append([name, price])
print(products)

#讓消費者輸入
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

#印出所有購買紀錄
for p in products:
    #print(p)
    print(p[0],'的價格是',p[1], '元')

#寫入檔案
with open ('products.csv', 'w', encoding='utf-8') as f :
    f.write('商品, 價格\n')
    for p in products:
        f.write(p[0]+','+p[1]+'\n')