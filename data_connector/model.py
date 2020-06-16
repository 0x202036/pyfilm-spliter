from abc import ABCMeta, abstractmethod


# 抽象类Model，不可被实例化，规定了所有Model子类共同拥有的环境（即数据库操作所需要的环境）
class Model(metaclass=ABCMeta):

    # 将目前的对象转化为插入sql指令（insert into ....）
    @abstractmethod
    def to_sql(self):
        pass
