import pymysql


class DataManager:

    def __init__(self, db_setting: dict):
        self.__server = db_setting['server']
        self.__user = db_setting['user']
        self.__password = db_setting['password']
        self.__database = db_setting['database']
        self.__connection = self.build_connection()

    # 与数据库建立连接
    def build_connection(self):
        return pymysql.connect(self.__server, self.__user, self.__password, self.__database)

    # 执行sql指令，注意只可以执行需要commit的指令，比如select查询等不能使用。
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

    # 在数据库中查询单词释义
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

    # 关闭与数据库的连接
    def close_connection(self):
        self.__connection.close()
