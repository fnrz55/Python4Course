from lab18.FileChanging import FileChaging

filename = "Nums.txt"

fc = FileChaging(filename, 5)
fc.fill_file_from_keyboard()

nums = fc.fill_list_from_file()
num_index = 0
result = 0
for num in nums:
    if num % 3 != 0:
        result += num % 3
    num_index += 1

print(f'Сумма остатков элементов = {result}')