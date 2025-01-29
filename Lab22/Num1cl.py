from typing import TypeVar, Generic

T = TypeVar('T')

class Num1(Generic[T]):

    def __init__(self, ob:T)->None:
        self.ob = ob

    def get_ob(self)->T:
        return self.ob

    def show_type(self)->None:
        print(f'Тип Т это {type(self.ob)}')