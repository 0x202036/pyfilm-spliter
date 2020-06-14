import analyser.caption
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
            if raw_caption != '':
                caption_list.append(analyser.caption.Caption(raw_caption))
        return caption_list

    @staticmethod
    def load_dir(path: str):
        film_list = []
        files = os.listdir(path)
        for file in files:
            if file.endswith(".srt"):
                film_list.append(CaptionFactory.load_srt_file(path+'\\'+file))
        return film_list

    @staticmethod
    def __load_file(path: str):
        file = open(path, 'rb')
        file_raw_lines = file.read()
        file.close()
        encoding_res = chardet.detect(file_raw_lines)
        return file_raw_lines.decode(encoding_res['encoding'], errors='ignore')
