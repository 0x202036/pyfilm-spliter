import data_connector.data_manager
import data_connector.model_sentence
import analyser.caption

dm = data_connector.data_manager.DataManager()
trans = dm.get_translation("WORK")
dm.close_connection()
print(trans)