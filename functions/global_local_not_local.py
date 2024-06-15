def f():
    global g
    l = 'i am local'

    print(g)
    print(l)

    def nested():
        nonlocal l
        print('i am non local from  parent:', l)
    nested()
g = 'i am global'
f()