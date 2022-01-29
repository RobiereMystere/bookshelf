class IsbnExtractor:
    @staticmethod
    def extract_from_file(filepath):
        content = ""
        with open(filepath, 'r') as file:
            content = file.read()
        return content.split("\n")
