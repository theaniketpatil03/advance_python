dic = {1: 2, 2: 3, 3: 4}

copy_dic = dic.copy()
print(copy_dic)

print(dic.get(5, 'None'))

print(dic.items())

print(dic.keys())

dic2 = {3: 10}
dic.update(dic2)
print(dic)

print(dic.values())

dic.pop(1) # pop whichever key we specify
print(dic)
dic.popitem() # pop from last
print(dic)

dic.clear()
print(dic)