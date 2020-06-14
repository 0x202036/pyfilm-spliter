import datetime


class Tick:

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, value: int):
        self.__hour = value

    @property
    def min(self):
        return self.__min

    @min.setter
    def min(self, value: int):
        self.__min = value

    @property
    def sec(self):
        return self.__sec

    @sec.setter
    def sec(self, value: int):
        self.__sec = value

    @property
    def min_sec(self):
        return self.__min_sec

    @min_sec.setter
    def min_sec(self, value: int):
        self.__min_sec = value

    def __init__(self, tick_string: str):
        tick_fragment = tick_string.split(':')
        sec_fragment = tick_fragment[2].split(',')
        self.__hour = int(tick_fragment[0])
        self.__min = int(tick_fragment[1])
        self.__sec = int(sec_fragment[0])
        self.__min_sec = int(sec_fragment[1])

    def __add_digital(self, num: int):
        return '0'+str(num) if(num < 10) else str(num)

    def __sub_digital(self, num: int):
        return str(num//10) if(num > 99) else str(num)

    def __hyper_time(self):
        return self.__add_digital(self.__hour*60+self.__min)

    def __str__(self):
        return self.__hyper_time() + ':'+self.__add_digital(self.__sec) + ":" + self.__sub_digital(self.__min_sec)

    def to_time(self):
        return datetime.time(hour=self.hour, minute=self.min, second=self.sec, microsecond=self.min_sec*1000)
