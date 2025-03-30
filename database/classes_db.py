from database.base_db import DatabaseManager

class ClassDB(DatabaseManager):
    def fetch_classes(self):
        query = """
        SELECT * FROM classes
        """
        return self.fetch_query(query)