import pymysql

from config.settings import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME


class DatabaseManager:
    def __init__(self):
        self.connection = None

    # 使用 with DatabaseManager() as db时自动调用此方法
    def __enter__(self):
        # print("进入__enter__方法")
        self.connection = self.create_connection()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()
        # print("退出__exit__方法")
    def create_connection(self):
        if not self.connection or not self.connection.open:
            try:
                self.connection = pymysql.connect(
                    host=DB_HOST,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    database=DB_NAME,
                    cursorclass=pymysql.cursors.DictCursor
                )
            except Exception as e:
                print("数据库连接失败", e)
        return self.connection
    def fetch_query(self, query, params=None, single=False):
        result = None
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute(query, params)
                    if single:
                        result = cursor.fetchone()
                    else:
                        result = cursor.fetchall()
            except Exception as e:
                print(f"查询错误：{e}")
        return result
    def execute_query(self, query, params=None):
        if self.connection:
            try:
                # 获取游标对象
                with self.connection.cursor() as cursor:
                    cursor.execute(query, params)
                    self.connection.commit() # 提交更改到数据库中（与查询不同）
                    return True
            except Exception as e:
                print(f"执行出错:{e}")
                self.connection.rollback() # 回滚数据库
                return None
        else:
            print("没有建立数据库连接！")
        return None
    def close_connection(self):
        if self.connection:
            self.connection.close()

if __name__ == '__main__':
    with DatabaseManager() as db:
        pass
