import analyser.caption
import data_connector.model_sentence
import chardet
import re
import os
import film_spliter.spliter


class CaptionFactory:

    @staticmethod
    def load_srt_file(path: str):
        caption_list = []
        regex = re.compile('^\r\n', re.M)
        file_lines = CaptionFactory.__load_file(path)
        for raw_caption in regex.split(file_lines):
            if raw_caption != '':
                temp_caption = analyser.caption.Caption(raw_caption)
                if CaptionFactory.__filter(temp_caption.english):
                    caption_list.append(temp_caption)
        return caption_list

    @staticmethod
    def load_dir(path: str, id: int, audio_path: str):
        sentence_list = []
        files = os.listdir(path)
        for file in files:
            if file.endswith(".srt"):
                is_have_film = CaptionFactory.__find_film(path, file)
                caption_list = CaptionFactory.load_srt_file(path + '\\' + file)
                if not is_have_film:
                    sentence_list += CaptionFactory.__build_sentence_list(id, caption_list, file[:-4])
                else:
                    film_source = path + '\\' + file[:-4] + ".mp4"
                    sentence_list += CaptionFactory.__build_sentence_list(id, caption_list, file[:-4], film_source, audio_path)
                id += len(caption_list)
        return sentence_list

    @staticmethod
    def __find_film(path, srt_name):
        is_found = False
        files = os.listdir(path)
        for file in files:
            if file.endswith(".mp4"):
                if file[: -4] == srt_name[: -4]:
                    is_found = True
                    break
        return is_found


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
        return len(sentence) > 10 and not re.search('[^A-z.?!\"&\'\- \r]', sentence)

    @staticmethod
    def __build_sentence_list(id: int, caption_list: list, f_name: str, source_film: str=None, target_audio: str=None):
        s_list = []
        for caption in caption_list:
            id += 1
            if source_film:
                audio_file = film_spliter.spliter.Spliter.split_to_mp3(source_film, target_audio, caption)
                s_list.append(
                    data_connector.model_sentence.ModelSentence(id, caption, f_name, target_audio + "\\" + audio_file))
            else:
                s_list.append(data_connector.model_sentence.ModelSentence(id, caption, f_name))
        return s_list

