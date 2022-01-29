from database_utils import DatabaseUtils


class DatabaseManager:
    def __init__(self):
        self.dbu = DatabaseUtils("data/bookshelf.db")
        self.dbu.create_table('author',
                              {'id': ['INTEGER ', 'PRIMARY KEY', 'AUTOINCREMENT', 'UNIQUE'],
                               'name': ['TEXT']})
        print(self.dbu.select('author'))
        self.dbu.create_table('book_author_relation',
                              {'id': ['INTEGER '],
                               'author_id': ['INTEGER '],
                               'book_id': ['INTEGER '],
                               'FOREIGN KEY(author_id)': ['REFERENCES author(id)'],
                               'FOREIGN KEY(book_id)': ['REFERENCES book(id)']
                               })
        print(self.dbu.select('book_author_relation'))

        self.dbu.create_table('book', {'id': ['INTEGER ', 'PRIMARY KEY', 'AUTOINCREMENT', 'UNIQUE'],
                                       'isbn': ['TEXT', 'UNIQUE'],
                                       'title': ['TEXT'],
                                       'book_author_relation': ['INTEGER '],
                                       'description': ['TEXT'],
                                       'language': ['TEXT'],
                                       'year': ['INTEGER']})
        print(self.dbu.select('book'))

        self.dbu.close()

    def add_item(self, table, values) -> int:
        """
        :param table:
        :param values:
        :return: id of inserted row
        """
        self.dbu.insert(table, values)
        return self.dbu.cursor.lastrowid

    def display_db(self):
        print(self.dbu.select('author'))
        print(self.dbu.select('book'))
        print(self.dbu.select('book_author_relation'))
