from analyser.analyser import *
from log_writer import *


if __name__ == '__main__':
    try:
        an = Analyser()
    except Exception as e:
        LogWriter.write_failed_doc(e)
    else:
        LogWriter.write_success_doc(str(len(an.word_list)), str(len(an.sentence_list)))
