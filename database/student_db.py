from database.base_db import DatabaseManager

class StudentDB(DatabaseManager):
    def fetch_students(self):
        query="""
                SELECT s.*, c.class_name, (s.chinese_score+s.math_score+s.english_score) as total_score
                FROM students s
                JOIN classes c ON s.class_id=c.class_id
            """
        return self.fetch_query(query)
    def add_student(self, student_info):
        # 添加一个学生
        query="""
            INSERT INTO students (student_name, student_number, gender, class_id, chinese_score, math_score, english_score)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            student_info["name"],
            student_info["number"],
            student_info["gender"],
            student_info["class_id"],
            student_info["chinese_score"],
            student_info["math_score"],
            student_info["english_score"]
        )
        self.execute_query(query, params)
    def student_number_exists(self, student_info):
        # 检查学号是否存在
        query = """
            SELECT COUNT(*) FROM students WHERE student_number=%s
        """
        params = (student_info["number"],)
        result = self.fetch_query(query, params, single=True)
        return result["COUNT(*)"] > 0

if __name__ == '__main__':
    with StudentDB() as db:
        students = db.fetch_students()
        print(students)