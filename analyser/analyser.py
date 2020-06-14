import analyser.caption_factory
import data_connector.model_sentence
import data_connector.model_word
import re


class Analyser:
    @property
    def sentence_list(self):
        return self.__sentence_list

    @sentence_list.setter
    def sentence_list(self, value):
        self.__sentence_list = value

    @property
    def word_list(self):
        return self.__word_list

    @word_list.setter
    def word_list(self, value):
        self.__word_list = value

    def __init__(self, dir: str, start_id: int = 0):
        self.__sentence_list = analyser.caption_factory.CaptionFactory.load_dir(dir, start_id)
        self.__word_list = []
        for sentence in self.__sentence_list:
            self.__split_word(sentence)

    def __split_word(self, sentence: data_connector.model_sentence.ModelSentence):
        # regex = re.compile(' ')
        # words = regex.split(sentence.s_en)
        words = sentence.s_en.split(' ')
        self.__judge_level(sentence, len(words))
        for word in words:
            is_include = False
            for word_model in self.__word_list:
                if word == word_model.word:
                    word_model.sentences += '|' + str(sentence.s_id)
                    is_include = True
            if not is_include:
                self.__word_list.append(data_connector.model_word.ModelWord(word, str(sentence.s_id)))

    def __judge_level(self, sentence: data_connector.model_sentence.ModelSentence, words_num: int):
        if words_num < 8:
            sentence.s_level = 0
        elif words_num < 16:
            sentence.s_level = 1
        else:
            sentence.s_level = 2
