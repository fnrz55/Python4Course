from lab18.FileChanging import FileChaging

filename = "Nums.txt"

fc = FileChaging(filename, 5)
fc.fill_file_from_keyboard()

nums = fc.fill_list_from_file()
num_index = 0
result = 0
for num in nums:
    if num * 4 > num ** 2:
        result += num
    num_index += 1

print(f'Сумма квадратов индексов = {result}')