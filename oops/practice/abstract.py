from abc import ABC, abstractmethod


class Computer(ABC):

    @abstractmethod
    def configuration():
        pass


class Lpatop(Computer):
    
    @property
    def prop():
        pass

lap1 = Lpatop()