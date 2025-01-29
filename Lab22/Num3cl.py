from typing import TypeVar, Generic
from numbers import Number

T = TypeVar('T', bound=Number)

class Num3(Generic[T]):

    def __init__(self, num:T)->None:
        self.num = num

    def recip(self)->Number:
        return 1 / float(self.num)

    def fraction(self)->Number:
        return float(self.num) - int(self.num)