import analyser.analyser

path = r'H:\开发\样本\film spliter\字幕原文件\Ant-Man.2015.720p.BluRay.x264-SPARKS.简体&英文.srt'
dir = r'H:\开发\样本\film spliter\字幕原文件'
dir2 = r'H:\开发\样本\film spliter\测试环境'

al = analyser.analyser.Analyser(dir)
print('the caption files have been analysed.')

