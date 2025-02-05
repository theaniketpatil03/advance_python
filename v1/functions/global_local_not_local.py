def f():
    global g
    l = 'i am local'

    print(g)
    print(l)
    x = 10
    def nested():
        # nonlocal l
        x +=1
        l += 'inner nested'
        print('i am non local from  parent:', l)
    nested()
g = 'i am global'
f()


def check():
    x = 10

    def inner_function():
        x+=1

        print(x)

    inner_function()
check()