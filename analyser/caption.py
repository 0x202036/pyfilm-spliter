from .tick import *
from functools import singledispatch


class Caption:
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: int):
        self.__id = value

    @property
    def start_tick(self):
        return self.__start_tick

    @start_tick.setter
    def start_tick(self, value: Tick):
        self.__start_tick = value

    @property
    def end_tick(self):
        return self.__end_tick

    @end_tick.setter
    def end_tick(self, value: Tick):
        self.__end_tick = value

    @property
    def english(self):
        return self.__english

    @english.setter
    def english(self, value: str):
        self.__english = value

    @property
    def chinese(self):
        return self.__chinese

    @chinese.setter
    def chinese(self, value: str):
        self.__chinese = value

    def __init_prop(self,caption_str: str):
        row_fragments = caption_str.split('\n')
        tick_fragments = row_fragments[1].split('-->')
        self.__id = int(row_fragments[0])
        self.__start_tick = Tick(tick_fragments[0])
        self.__end_tick = Tick(tick_fragments[1])
        self.__chinese = row_fragments[2].replace('\r', '')
        self.__english = row_fragments[3].replace('\r', '')

    @singledispatch
    def __init__(self, caption_str: str=None):
        if caption_str is not None:
            self.__init_prop(caption_str)
        else:
            self.__id = 0
            self.__start_tick = Tick()
            self.__end_tick = Tick()
            self.__chinese = ""
            self.__english = ""

    def __add__(self, other):
        c_new = Caption()
        c_new.id = self.id
        c_new.start_tick = self.start_tick
        c_new.end_tick = other.end_tick
        c_new.english = self.english + ' ' + other.english
        c_new.chinese = self.chinese + ' ' + other.chinese
        return c_new

    def __bool__(self):
        return bool(self.english)

    def __str__(self):
        return self.english
