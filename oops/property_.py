class Fruit:

    def __init__(self, name) -> None:
        self._name = name

    @property
    def fruit_name(self):
        return self._name

    @fruit_name.setter
    def fruit_name(self, value):
        self._name = value
        return 'name changed'

    @fruit_name.deleter
    def fruit_name(self):
        del self._name
        return 'name deleted'


bana = Fruit('banana')
print(dir(bana))
print(bana.fruit_name)
bana.fruit_name = 'orange'
print(bana.fruit_name)

del bana.fruit_name
print(bana.fruit_name)
    

