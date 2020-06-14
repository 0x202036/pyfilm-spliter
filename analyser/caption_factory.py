import analyser.caption
import data_connector.model_sentence
import chardet
import re
import os


class CaptionFactory:

    @staticmethod
    def load_srt_file(path: str):
        caption_list = []
        regex = re.compile('^\r\n', re.M)
        file_lines = CaptionFactory.__load_file(path)
        for raw_caption in regex.split(file_lines):
            if CaptionFactory.__filter(raw_caption):
                caption_list.append(analyser.caption.Caption(raw_caption))
        return caption_list

    @staticmethod
    def load_dir(path: str, id: int):
        sentence_list = []
        files = os.listdir(path)
        for file in files:
            if file.endswith(".srt"):
                caption_list = CaptionFactory.load_srt_file(path + '\\' + file)
                sentence_list += CaptionFactory.__build_sentence_list(id, caption_list, file[:-4])
                id += len(caption_list)
        return sentence_list

    @staticmethod
    def __load_file(path: str):
        file = open(path, 'rb')
        file_raw_lines = file.read()
        file.close()
        encoding_res = chardet.detect(file_raw_lines)
        return file_raw_lines.decode(encoding_res['encoding'], errors='ignore')

    #过滤句子，筛选掉不能加入数据库的句子。改写and后的true实现
    @staticmethod
    def __filter(sentence: str):
        return sentence != '' and True

    @staticmethod
    def __build_sentence_list(id: int, caption_list: list, f_name: str):
        s_list = []
        for caption in caption_list:
            id += 1
            s_list.append(data_connector.model_sentence.ModelSentence(id, caption, f_name))
        return s_list

