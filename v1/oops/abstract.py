'''
a method which has declaration but not body or statement then it is call abstract method
so the class which has abstract method is call abstract class
'''
# to make class truly abstract - it just makes some methods compulsary for child class

from abc import ABC, abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(slef):
        pass

class Laptop(Computer):

    def process(self):
        pass

lap = Laptop()

