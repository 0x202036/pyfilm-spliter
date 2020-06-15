import analyser.analyser
import analyser.caption_factory
import data_connector.data_manager
import film_spliter.spliter

path = r'H:\开发\样本\film spliter\Forrest\Forrest.Gump.1994.REMASTERED.1080p.BluRay.X264-AMIABLE.简体&英文.srt'
dir = r'H:\开发\样本\film spliter\字幕原文件'
dir2 = r'H:\开发\样本\film spliter\测试环境'
film = r'I:\电影\Forrest.Gump.1994.REMASTERED.1080p.BluRay.X264-AMIABLE.mp4'
audio = r'H:\开发\样本\film spliter\audio'

al = analyser.analyser.Analyser(dir2, audio)
print('the caption files have been analysed.')
# dm = data_connector.data_manager.DataManager()
# res = dm.execute_sql(al.sentence_list[50].to_sql())
# c_list = analyser.caption_factory.CaptionFactory.load_srt_file(path)
# res = film_spliter.spliter.Spliter.split_to_mp3(20, film, dir2, c_list[20])
print("done!")

