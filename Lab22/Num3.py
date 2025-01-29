from Lab22.Num3cl import Num3

iOb = Num3[int](5)
print(f'Обратная величина iOb{iOb.recip()}')
print(f'Дробная величина iOb{iOb.recip()}')
fOb = Num3[float](5.25)
print(f'Обратная величина fOb{fOb.recip()}')
print(f'Дробная величина fOb{fOb.recip()}')
sOb = Num3[str]('Ошибка')
sOb.recip()
