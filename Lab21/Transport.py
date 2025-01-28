from enum import Enum


class Transport(Enum):
    CAR = (3, "Автомобиль переозит людей")
    TRACK = (5, "Грузовики предназначены для перевозки грузов . В них путешествовать некомфортно, но если "
                "зажмуриться, то можно. Но, к сожалению, наша компания таких услуг не предоставляет. Рекомендуем вам "
                "обратить внимание на другой вид транспорта")
    PLANE = (4, "Самолет летит")
    TRAIN = (3, "Поезд движется по рельсам")
    BOAT = (6, "Лодка плывет по воде")
    BUS = (2, "Автобус")

    def __init__(self, cost, message):
        self.cost = cost
        self.message = message

    def get_message(self):
        return self.message

    def get_cost(self):
        return self.cost

    def get_by_index(idx):
        return list(Transport)[idx]
