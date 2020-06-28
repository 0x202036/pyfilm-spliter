import time
import traceback
import os


class LogWriter:

    file_name = "runtime_doc.txt"

    @staticmethod
    def write_warning(e: Exception, warning: str):
        content = "Warning!\n警告内容：\t%s\n错误类型str(Exception):\t%s\n友好提示str(e):\t%s\n详细错误类型repr(e):\t%s\ntraceback.print_exc():\t%s\n异常链traceback.format_exc():\n%s\n" % \
                  (warning, str(Exception), str(e), repr(e), traceback.print_exc(), traceback.format_exc())
        LogWriter.__write_doc(content)

    @staticmethod
    def write_success_doc(word_count: str, sentences_count: str):
        content = 'Done!\nword_count:\t%s\nsentence_count:\t%s\nAll data have been uploaded in database.\n$END$' % \
                  (word_count, sentences_count)
        LogWriter.__write_doc(content)

    @staticmethod
    def write_failed_doc(e: Exception):
        content = 'Exception Happened:\n错误类型str(Exception):\t%s\n友好提示str(e):\t%s\n详细错误类型repr(e):\t%s\ntraceback.print_exc():\t%s\n异常链traceback.format_exc():\n%s\n$END$' % \
            (str(Exception), str(e), repr(e), traceback.print_exc(), traceback.format_exc())
        LogWriter.__write_doc(content)

    @staticmethod
    def __write_doc(content_str: str):
        content = 'date:' + time.asctime(time.localtime(time.time())) + '\n' \
                                                                        '================================================\n' + content_str
        LogWriter.__write(content)

    @staticmethod
    def __write(content: str):
        if LogWriter.__is_end():
            doc_file = open('runtime_doc.txt', 'w', encoding='utf-8')
        else:
            doc_file = open('runtime_doc.txt', 'a', encoding='utf-8')
        doc_file.write(content)
        doc_file.close()

    @staticmethod
    def __is_end():
        res = True
        if os.path.exists(LogWriter.file_name):
            file = open(LogWriter.file_name, "rb")
            file.seek(-5, 2)
            if not file.read(5).decode("utf-8") == "$END$":
                res = False
        return res

