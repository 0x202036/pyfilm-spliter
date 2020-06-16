from xml.etree.ElementTree import *



def decode_xml(self):
    setting = parse('.\\setting.xml')
    for item in setting.iterfind('path'):
        caption_path = item.findtext('caption_path')
    print(caption_path)

