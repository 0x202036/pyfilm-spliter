from .tick import *


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

    def __init__(self, caption_str: str):
        row_fragments = caption_str.split('\n')
        tick_fragments = row_fragments[1].split('-->')
        self.__id = int(row_fragments[0])
        self.__start_tick = Tick(tick_fragments[0])
        self.__end_tick = Tick(tick_fragments[1])
        self.__chinese = row_fragments[2].replace('\r', '')
        self.__english = row_fragments[3].replace('\r', '')
