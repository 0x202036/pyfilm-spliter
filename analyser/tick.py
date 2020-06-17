# 一个重构的时间类，通过str可以得到moviepy裁切电影的标准时刻字符串
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

    def __init_prop(self, tick_string: str):
        tick_fragment = tick_string.split(':')
        sec_fragment = tick_fragment[2].split(',')
        self.__hour = int(tick_fragment[0])
        self.__min = int(tick_fragment[1])
        self.__sec = int(sec_fragment[0])
        self.__min_sec = int(sec_fragment[1])

    def __init__(self, tick_string: str=None):
        if tick_string is not None:
            self.__init_prop(tick_string)
        else:
            self.__hour = 0
            self.__min = 0
            self.__sec = 0
            self.__min_sec = 0

    def __sub_digital(self, num: int):
        return str(num//10) if(num > 99) else str(num)

    def __str__(self):
        return str(self.__hour) + ":" + str(self.__min) + ":" + str(self.__sec) + '.' + self.__sub_digital(self.__min_sec)

    def __add__(self, other):
        t_new = Tick()
        t_new.hour = self.hour + other.hour
        t_new.min = self.min + other.min
        t_new.sec = self.sec + other.sec
        t_new.min_sec = self.min_sec + other.min_sec
        return t_new
