import sqlite3


class DatabaseManager:
    def __init__(self, db_path: str):
        self.connection = sqlite3.connect(db_path)
        self.cur = self.connection.cursor()

    def close(self):
        """close sqlite3 connection"""
        self.connection.close()

    def execute(self, query: str):
        """execute a row of data to current cursor"""
        self.cur.execute(query)

    def insert(self, table, values):
        """add many new data to database in one go"""
        self.create_table()
        query = 'INSERT INTO ' + table + ' VALUES'
        for value in range(len(values) - 1):
            query += values + ','
        query += values[-1] + ')'
        print(query)
        self.cur.executemany(query, values)

    def create_table(self, table_name: str, table_dict: dict):
        """create a database table if it does not exist already"""
        # TO-DO
        """table_dict must be formalised like this : {'attribute1':[type,constraints,...]}"""
        query = "CREATE TABLE IF NOT EXISTS " + table_name + "("
        for key, values in table_dict.items():
            query += key + ' '
            for value in values:
                query += value + ' '
            pass
        query += ")"
        print(query)
        self.cur.execute(query)

    def commit(self):
        """commit changes to database"""
        self.connection.commit()
