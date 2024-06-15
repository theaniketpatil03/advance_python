'''
{(condition1 :  <code1>) , (condition2 :  <code2>) }.get(True, <code3>)
'''

x = 0
result = {x > 0: 'positive', x == 0: 'negitive'}.get(True, "Zero")
print(result)

if x < 0:
    print('doomed')