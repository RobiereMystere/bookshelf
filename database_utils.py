import sqlite3


class DatabaseUtils:
    def __init__(self, db_path: str):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def close(self):
        """close sqlite3 connection"""
        self.connection.close()

    def execute(self, query: str):
        """execute a row of data to current cursor"""
        self.cursor.execute(query)

    def insert(self, table: str, values: list):
        """add many new data to database in one go"""
        query = 'INSERT INTO ' + table + ' VALUES ('
        for value in values[:-1]:
            v = value

            if type(v) == str:
                v = '"' + v + '"'
            query += str(v) + ','
        v = values[-1]
        if type(v) == str:
            v = '"' + v + '"'
        query += str(v) + ')'
        print(query)
        self.execute(query)

    def create_table(self, table_name: str, table_dict: dict):
        """create a database table if it does not exist already"""
        """table_dict must be formalised like this : {'attribute1':[type,constraints,...]}"""
        query = "CREATE TABLE IF NOT EXISTS " + table_name + "("
        for key, values in table_dict.items():
            query += key + ' '
            for value in values:
                query += value + ' '
            query += ', '
        query = query[:-2] + ")"
        print(query)
        self.cursor.execute(query)

    def select(self, table, column='*'):
        self.cursor.execute("SELECT " + column + " FROM " + table)
        return self.cursor.fetchall()

    def last_id(self, table):
        self.cursor.execute("SELECT * FROM " + table + " ORDER BY id DESC LIMIT 1")
        last_id = self.cursor.fetchone()
        if last_id is None:
            return -1
        return int(last_id[0])

    def commit(self):
        """commit changes to database"""
        self.connection.commit()