import os
from xml.etree.ElementTree import *
# 这是一个自动重命名工具，由于本软件只接受中英共有的字幕，此类字幕下载后均有'.简体&英文'后缀，
# 若不去除则会被当作电影名的一部分上传到数据库，需用此工具自动命名才能分析
# 这里默认的字幕位置是setting中的caption_path


def decode_xml():
    setting = parse('setting.xml')
    path = None
    for item in setting.iterfind('path'):
        path = item.findtext('caption_path')
    return path


if __name__ == '__main__':
    path = decode_xml()
    files = os.listdir(path)
    for file in files:
        if '.简体&英文' in file:
            old = file
            new = file.replace('.简体&英文', '')
            os.rename(path+'\\'+file, path+'\\'+new)
            print(old+'----->'+new)
    print('all done!')
