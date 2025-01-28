from enum import Enum


class TrafficLightColor(Enum):
    RED = (12, "Красный")
    YELLOW = (2, "Желтый")
    GREEN = (10, "Зеленый")
    YELLOW_GREEN = (5, "Желтый")

    def __init__(self, time, name):
        self.time = time
        self.color_name = name

    def get_time(self):
        return self.time

    def get_name(self):
        return self.color_name
