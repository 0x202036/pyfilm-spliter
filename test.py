import data_connector.data_manager
import data_connector.model_sentence
import analyser.caption
import re

# dm = data_connector.data_manager.DataManager()
# trans = dm.get_translation("WORK")
# dm.close_connection()
# print(trans)
regex = re.compile('[^A-z.?!\"&\'\- ]')
res = regex.search("You're supposed to be in Moscow.{")
print(bool(res))