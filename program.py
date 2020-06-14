import analyser.caption_factory

path = r'H:\开发\样本\film spliter\字幕原文件\Ant-Man.2015.720p.BluRay.x264-SPARKS.简体&英文.srt'
dir = r'H:\开发\样本\film spliter\字幕原文件'

file_list = analyser.caption_factory.CaptionFactory.load_dir(dir)
print('the caption files had been loaded.')

