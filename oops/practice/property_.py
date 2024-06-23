class Fruit:

    def __init__(self, name) -> None:
        self._name = name
        self._game = 'game'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value in ['orange', 'apple']:
            self._name = value
            return 'name changed'

    @name.deleter
    def fruit_name(self):
        del self._name
        return 'name deleted'


bana = Fruit('banana')
# print(dir(bana))
print(bana.name)
bana.name = 'kela'
print(bana.name)

# del bana.name
# print(bana.fruit_name)

bana._name = 'kela'
print(bana._name)
    

print(dir(bana))