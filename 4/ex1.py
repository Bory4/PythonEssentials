def data_input():
    data = input("Give me product name, category and price in following format:\nproduct, category, price\n> ")
    temp = data.strip().split(",")
    
    # Done like that for code visibility and readability    
    
    name = temp[0].strip()
    category = temp[1].strip()
    price = int(temp[2].strip())
    
    return (name, category, price)

def list_maker(num):
    products = []
    for i in range(num):
        products.append(data_input())
    return products

def dict_maker(product_list):
    category = {}
    for i in product_list:
        if i[1] in category:
            category[i[1]].append(i[0])
        else:
            category[i[1]] = [i[0]]
    return category

def displayer(productCategory, productList):
    temp = productList[productCategory]
    for i in temp:
        print(i)

aaa = list_maker(3)
bbb = dict_maker(aaa)
displayer("bbb", bbb)
