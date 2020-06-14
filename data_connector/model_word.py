import data_connector.model


class ModelWord(data_connector.model.Model):
    @property
    def word(self):
        return self.__word

    @word.setter
    def word(self, value: str):
        self.__word = value

    @property
    def translation(self):
        return self.__translation

    @translation.setter
    def translation(self, value: str):
        self.__translation = value

    @property
    def sentences(self):
        return self.__sentences

    @sentences.setter
    def sentences(self, value: str):
        self.__sentences = value

    def __init__(self, word: str, sentences: str):
        self.__word = word
        self.__sentences = sentences
