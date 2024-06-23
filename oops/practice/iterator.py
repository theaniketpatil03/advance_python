class Iterator:
    def __init__(self, limit) -> None:
        self.limit = limit

    def __iter__(self):
        self.stop = 0
        return self

    def __next__(self):
        stop = self.stop

        if stop >= self.limit:
            raise StopIteration
        
        self.stop = stop + 1
        return stop

its = Iterator(15)

print(its)