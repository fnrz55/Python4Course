from Lab22.Num2cl import Num2

thObj = Num2[int, str](6, 'тест обобщений')

thObj.show_types()
v = thObj.get_ob()
print(f'Значение v - {v}')
str1 = thObj.get_ob2()
print(f'Значение str1 - {str1}')
