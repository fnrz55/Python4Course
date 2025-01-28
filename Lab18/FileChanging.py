class FileChaging:
    def __init__(self, filename, elements_num):
        self.filename = filename
        self.elements_num = elements_num

    def fill_file_from_keyboard(self):
        with open(self.filename, 'w') as f:
            input_num = 1
            while input_num <= self.elements_num:
                current_num = input(f'Введите {input_num}ое число')
                try:
                    int(current_num)
                    if input_num == self.elements_num:
                        current_num = str(current_num)
                    else:
                        current_num = str(current_num) + ","
                    f.write(current_num)
                except ValueError:
                    input_num -= 1
                    print('Введено не число')
                input_num += 1

    def fill_list_from_file(self):
        with open(self.filename) as f:
            file_data = f.read()
            file_data_list = file_data.split(",")
            file_data_list = [int(item) for item in file_data_list]

            return file_data_list