from analyser.analyser import *
import traceback
import time

def write_doc(content_str: str):
    content = 'date:'+time.asctime(time.localtime(time.time()))+'\n' \
              '================================================\n'+ content_str
    doc_file = open('runtime_doc.txt', 'w', encoding='utf-8')
    doc_file.write(content)
    doc_file.close()

try:
    an = Analyser()
except Exception as e:
    c = 'Exception Happened:\nstr(Exception):\t%s\nstr(e):\t%s\nrepr(e):\t%s\ntraceback.print_exc():\t%s\ntraceback.format_exc():\n%s' % \
        (str(Exception), str(e), repr(e), traceback.print_exc(), traceback.format_exc())
    write_doc(c)
else:
    c = 'Done!\nword_count:\t%s\nsentence_count:\t%s\nAll data have been uploaded in database.' % \
        (str(len(an.word_list)), str(len(an.sentence_list)))
    write_doc(c)