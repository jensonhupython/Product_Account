# 新增檢查檔案是否存在
import os # operating system

#products = []
# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f: 
        for line in f:
            #split_s = line.strip().split(',')
            #split_s_name = split_s[0]
            #split_s_price = split_s[1]
            # can merge to do
            if '商品,價格' in line: 
                continue
            split_s_name, split_s_price = line.strip().split(',')
            products.append([split_s_name, split_s_price])    
    return products            
#檢查檔案是否存在
#if os.path.isfile('products.csv'):
#    print('Yes!!')
    
# 讀取檔案 (取出商品名稱)
# 讀取檔案要注意換行符號要去除掉 strip
# use continue to ignore the specific word  
#def read_file(filename):
#    if os.path.isfile(filename): #檢查檔案在不在
#        print('檔案存在!!') 


#        print(products)    
#    else:
#        print('No 找不到檔案!!!')
#    return products

# 1. GitHub 建立專案
# 2. 撰寫程式碼
# 3. 二維清單
# 4. 存取二維清單
# 5. for loop 搞清楚每個東西是什麼

# Think: How to 增加輸入價格到 products 清單裡面
# 先拿一個新的小清單, 然後再append到大清單

#products = []
# 讓使用者輸入
def user_input(products):
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
    return(products)
# Think: How to 存取二維清單
# products[0][0]
#print('商品名稱: ', products[0][0], '商品價格: ', products[0][1])

# for loop 印出清單中的每一個商品名稱跟價格
def print_products(products):
    for p in products: 
        #print(p)
        print(p[0], '的價格: ', p[1])

# 寫入檔案, 檔案名稱常使用 .csv file, csv file 需用逗點做區隔
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品, 價錢\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')



def main():
    filename = 'products.csv'
    #products = []
    if os.path.isfile(filename): #檢查檔案在不在
        print('檔案存在!!')
        products = read_file(filename)
        print(products)
    else: 
        print('找不到檔案!!')    
        products = []
        products = user_input(products)
        print_products(products)
        write_file('products.csv', products)

#if __name__ == '__main__':
# main function 程式進入點
main()











