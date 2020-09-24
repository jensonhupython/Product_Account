# 1. GitHub 建立專案
# 2. 撰寫程式碼
# 3. 二維清單
# 4. 存取二維清單
# 5. for loop 搞清楚每個東西是什麼

# Think: How to 增加輸入價格到 products 清單裡面
# 先拿一個新的小清單, 然後再append到大清單

products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    price = int(price)
    #p = []
    #p.append(name)
    #p.append(price)
    #簡潔寫法
    #p = [name, price]
    #更簡潔寫法
    products.append([name, price])
    #products.append(name) 
    #products.append(p)
print(products)    

# Think: How to 存取二維清單
# products[0][0]
#print('商品名稱: ', products[0][0], '商品價格: ', products[0][1])

# for loop 印出清單中的每一個商品名稱跟價格
for p in products: 
    #print(p)
    print(p[0], '的價格: ', p[1])

# 寫入檔案, 檔案名稱常使用 .csv file, csv file 需用逗點做區隔
with open('products.csv', 'w') as f:
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')













