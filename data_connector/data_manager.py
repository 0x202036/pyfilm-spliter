import pymysql


class DataManager:
    server = '127.0.0.1'
    user = 'root'
    password = 'root'
    database = 'words'

    def __init__(self):
        self.__connection = self.build_connection()

    def build_connection(self):
        return pymysql.connect(self.server, self.user, self.password, self.database)

    def execute_sql(self, sql: str):
        cursor = self.__connection.cursor()
        is_success = False
        try:
            cursor.execute(sql)
            self.__connection.commit()
            is_success = True
        except:
            self.__connection.rollback()
        return is_success

    def get_translation(self, word: str):
        if "\'" in word:
            return None
        cursor = self.__connection.cursor()
        cursor.execute("select translation from enwords where word='%s'" % word)
        try:
            res_data = str(cursor.fetchone()[0])
        except TypeError:
            res_data = None
        return res_data

    def close_connection(self):
        self.__connection.close()
