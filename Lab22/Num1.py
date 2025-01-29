from Lab22.Num1cl import Num1

iOb = Num1[int](6)
iOb.show_type()
v = iOb.get_ob()
print(f'Значение v - {v}')
strOb = Num1[str]("Строка")
strOb.show_type()
str1 = strOb.get_ob()
print(f'Значение str1 - {str1}')
