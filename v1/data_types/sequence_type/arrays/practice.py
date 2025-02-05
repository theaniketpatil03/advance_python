import array


a = array.array('i',  [2, 3, 4, 5, 6, 7, 8])

print(a)
a[2] = 10
print(a)

a.append(11)
print(a)

a.insert(5, 50)
print(a)

a.pop()
print(a)

a.remove(50)
print(a)

print(a.index(5))

a.reverse()
print(a)

a.extend([6, 67])
print(a)


b = array.array('d', [2.3, 2, 1])
print(b)

