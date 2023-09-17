def getDict(nkeys):
    r={}
    for _ in range(nkeys):
        print('Enter key (empty enter - exit)')
        k=input()
        if k=='':
            break
        print('Enter value')
        v=input()
        r[k]=v
    return r

def flip_kv_vk(dict_1):
    x={v:k for k,v in dict_1.items()}
    return x

print("Введите колличество пар в словаре")
n=int(input())
dict_1=getDict(n)
print("Ваш словарь", dict_1)
per=flip_kv_vk(dict_1)
print("Перевернутый словарь:",per)
print(flip_kv_vk({'3': 'fsdfg', '5': 'dfxdgh', '1': 'xdfg'}))