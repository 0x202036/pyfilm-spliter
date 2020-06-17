import re
from .caption import Caption


class CaptionMerger:
    @property
    def merge_result(self):
        return self.__merge_result

    def __init__(self):
        self.__fore_caption = Caption()
        self.__merge_result = []
        self.__merge_count = 0

    def merge_caption(self, c: Caption):
        reg = re.compile('[.!]$|(.")$|(!")$')
        if self.__fore_caption:
            if reg.search(str(c)):
                self.__add_caption(self.__fore_caption + c)
            else:
                self.__merge_middle_caption(c)

        else:
            if reg.search(str(c)):
                self.__add_caption(c)
            else:
                self.__fore_caption = c

    def __add_caption(self, c: Caption):
        if c not in self.__merge_result:
            self.__merge_result.append(c)
            self.__fore_caption = Caption()
            self.__merge_count = 0

    def __merge_middle_caption(self,c: Caption):
        self.__merge_count += 1
        if len(str(self.__fore_caption)) > 100:
            if self.__merge_count > 3:
                self.__add_caption(c)
            else:
                self.__fore_caption += c
        else:
            self.__fore_caption += c