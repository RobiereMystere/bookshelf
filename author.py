class Author:
    author_id: int
    name: str

    def __init__(self, author_id, name):
        self.author_id = author_id
        self.name = name

    def __str__(self):
        return self.name
