from abc import ABC, abstractmethod


class Database(ABC):
    def register(self, host, user, password):
        print("Host : {}".format(host))
        print("User : {}".format(user))
        print("Password : {}".format(password))
        print("Register Success!")

    @abstractmethod
    def query(self, *args):
        """
        传入查询数据的SQL语句并执行
        """

    @abstractmethod
    def execute(sql_string):
        """
        执行SQL语句
        """


class Component1(Database):
    def __init__(self, host, user, password):
        self.register(host, user, password)

    @staticmethod
    def execute(sql_string):
        print(sql_string)


    def query(self, *args):
        sql_string = "SELECT ID FROM db_name"
        self.execute(sql_string)


class Component2(Database):
    def __init__(self, host, user, password):
        self.register(host, user, password)

    @staticmethod
    def execute(sql_string):
        print(sql_string)

    def query(self, *args):
        sql_string = "SELECT NAME FROM db_name"
        self.execute(sql_string)


if __name__ == '__main__':
    comp1 = Component1("00.00.00.00", "abc", "000000")
    comp2 = Component2("11.11.11.11", "ABC", "111111")
    comp1.query()
    comp2.query()