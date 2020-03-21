class Tick:
    __hour=0
    __min = 0
    __sec = 0
    __min_sec = 0

    def __init__(self, tick_string):
        tick_fragment = tick_string.split(':')
        sec_fragment = tick_fragment[2].split(',')
        self.__hour = int(tick_fragment[0])
        self.__min = int(tick_fragment[1])
        self.__sec = int(sec_fragment[0])
        self.__min_sec = int(sec_fragment[1])

    def __add_digital(self,num):
        return '0'+str(num) if(num < 10) else str(num)

    def __sub_digital(self,num):
        return str(num//10) if(num > 99) else str(num)

    def __hyper_time(self):
        return self.__add_digital(self.__hour*60+self.__min)

    def __str__(self):
        return self.__hyper_time() + ':'+self.__add_digital(self.__sec) + ":" + self.__sub_digital(self.__min_sec)
