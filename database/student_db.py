from database.base_db import DatabaseManager

class StudentDB(DatabaseManager):
    def fetch_students(self):
        query="""
                SELECT s.*, c.class_name, (s.chinese_score+s.math_score+s.english_score) as total_score
                FROM students s
                JOIN classes c ON s.class_id=c.class_id
            """
        return self.fetch_query(query)

if __name__ == '__main__':
    with StudentDB() as db:
        students = db.fetch_students()
        print(students)