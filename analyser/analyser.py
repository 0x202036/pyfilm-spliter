import analyser.caption_factory
import data_connector.model_sentence
import data_connector.model_word
import data_connector.data_manager
from xml.etree.ElementTree import *
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

    def __init__(self, start_id: int = 0):
        self.__db_setting = self.__decode_xml()
        print('分解字幕文件并分割视频....')
        self.__sentence_list = analyser.caption_factory.CaptionFactory.load_dir(self.__caption_path, start_id, self.__audio_path)
        self.__word_list = []
        dm = data_connector.data_manager.DataManager(self.__db_setting)
        print('分析例句并上传....')
        for sentence in self.__sentence_list:
            self.__split_word(sentence)
            dm.execute_sql(sentence.to_sql())
        print('上传分析结果....')
        for word in self.__word_list:
            dm.execute_sql(word.to_sql())
        dm.close_connection()
        print('作业结束。')

    # 从例句中分割出单词并保存
    def __split_word(self, sentence: data_connector.model_sentence.ModelSentence):
        words = sentence.s_en.split(' ')
        dm = data_connector.data_manager.DataManager(self.__db_setting)
        for word in words:
            clean_word = re.sub('[,.!?:]', '', word.lower())
            trans = dm.get_translation(clean_word)
            if trans:
                is_include = False
                for word_model in self.__word_list:
                    if clean_word == word_model.word:
                        word_model.sentences += '|' + str(sentence.s_id)
                        is_include = True
                if not is_include:
                    self.__word_list.append(data_connector.model_word.ModelWord(clean_word, str(sentence.s_id), trans))
        dm.close_connection()

    # 解析xml文件
    def __decode_xml(self):
        db_setting = {}
        setting = parse('.\\setting.xml')
        for item in setting.iterfind('path'):
            self.__caption_path = item.findtext('caption_path')
            self.__audio_path = item.findtext('audio_path')
        for item in setting.iterfind('database'):
            db_setting.update({'server': item.findtext('server')})
            db_setting.update({'user': item.findtext('user')})
            db_setting.update({'password': item.findtext('password')})
            db_setting.update({'database': item.findtext('db_name')})
        return db_setting
