x = 120

match x:
    case x if x > 100:
        print('x greater than 100')

    case _:
        print('nothing')



point = (2, 2)

match point:
    # case (2, 3):
    #     print('exact match')

    case (x, y) if x == y:
        print('both values are same')


data = ("status", 200, {"user": "Alice"})

match data:
    case ("status", 200, {"user": user}):
        print(f"User is {user} and status is OK")
    case ("status", 404, _):
        print("Status not found")
    case _:
        print("Unknown status")


obj = ("status", 400, {'user': 'kunal'})

match obj:
    case ('status', 200, {'use': anything}):
        print(f'status ok with {anything}')

    case ('status', 400, _):
        print('error 400')

    case _ :
        print('unknown status')




lets = {'user': 'aniket', 'status': 300}

match lets:
    case {'user': anyuser, 'status': 500}:
        print(f"status 500 for {anyuser}")

    case {'status': 300, **anyother}:
        print('status 300 error')


lists = [2, 3, 4]

match lists:
    case [2, *_]: # * for rest of values or you have to define _ for all values
        print('2 in list')
    case [_, 3, _]:
        print('3 at post 1')




shape = {'type': 'circle', 'radius': 5}

match shape:
    case {'type': 'circle', 'radius': r}:
        print(f"circle with radius {r}")

    case {'type': 'square', 'side': s }:
        print(f'square with side {s}')
    # case {'type': 'square', 'side': _ }: # underscore ( _ ) is not define error at print
    #     print(f'square with side {_}')