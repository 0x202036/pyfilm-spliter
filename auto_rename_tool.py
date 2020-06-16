import os
from xml.etree.ElementTree import *


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
