from typing import TypeVar, Generic

T = TypeVar('T')
V = TypeVar('V')

class Num2(Generic[T, V]):

    def __init__(self, ob:T, ob2:V)->None:
        self.ob = ob
        self.ob2 = ob2

    def get_ob(self)->T:
        return self.ob

    def get_ob2(self)->V:
        return self.ob2

    def show_types(self)->None:
        print(f'Тип Т это {type(self.ob)}')
        print(f'Тип V это {type(self.ob2)}')