import sys

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QApplication, QTableWidget, QHeaderView, QCheckBox, \
    QTableWidgetItem
from qfluentwidgets import CardWidget, PushButton, SearchLineEdit, TableWidget, setCustomStyleSheet

from database.student_db import StudentDB
from student.student_dialog import AddStudentDialog
from utils.custom_style import ADD_BUTTON_STYLE, BATCH_DELETE_BUTTON_STYLE


class StudentInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("StudentInterface")
        self.setup_ui()
        self.load_data()
        self.populate_table()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        # 顶部按钮组
        card_widget = CardWidget(self)
        buttons_layout = QHBoxLayout(card_widget) # 按钮组归属于card_widget

        self.addButton = PushButton("新增", self)
        setCustomStyleSheet(self.addButton, ADD_BUTTON_STYLE, ADD_BUTTON_STYLE)

        self.addButton.clicked.connect(self.add_student)
        self.searchInput = SearchLineEdit(self)
        self.searchInput.setFixedWidth(500)
        self.searchInput.setPlaceholderText("搜索学生姓名或学号...")
        self.batchDeleteButton = PushButton("批量删除", self)
        setCustomStyleSheet(self.batchDeleteButton, BATCH_DELETE_BUTTON_STYLE, BATCH_DELETE_BUTTON_STYLE)


        buttons_layout.addWidget(self.addButton)
        buttons_layout.addWidget(self.searchInput)
        buttons_layout.addStretch() # 填充一个空组件
        buttons_layout.addWidget(self.batchDeleteButton)
        layout.addWidget(card_widget)

        # 添加表格组件
        self.table_widget = TableWidget(self)
        self.table_widget.setBorderRadius(8) #设置表格圆角
        self.table_widget.setBorderVisible(True)## 设置表格边框可见
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch) # 设置填充满表格表头

        ## 设置表头
        self.table_widget.setColumnCount(11)
        self.table_widget.setHorizontalHeaderLabels(["","学生ID", "姓名", "学号", "性别", "班级", "语文", "数学", "英语", "总分", "操作"])

        layout.addWidget(self.table_widget)

        # 设置背景为白色
        self.setStyleSheet("StudentInterface {background: white}")
        self.resize(1280,768)
        self.show()

    def add_student(self):
        """添加学生信息"""
        dialog = AddStudentDialog(self)
        if dialog.exec():
            print("用户点击了确定按钮")
        else:
            print("用户点击了取消按钮")

    # 加载数据
    def load_data(self):
        self.column_lis = ['student_id', 'student_name', 'student_number', 'gender', 'class_id', 'chinese_score', 'math_score', 'english_score', 'total_score']
        with StudentDB() as db:
            self.students = db.fetch_students()
        # self.student = [
        #     {"student_id": 1, "student_name": "张三", "student_number": 20241201, "gender":1, "class_id": 1, "chinese_score   ": 90, "math_score": 80, "english_score": 70, "total_score": 240},
        #     {"student_id": 2, "student_name": "张三", "student_number": 20241201, "gender":1, "class_id": 1, "chinese_score   ": 90, "math_score": 80, "english_score": 70, "total_score": 240}
        # ]
    # 展示表格信息
    def populate_table(self):
        self.table_widget.setRowCount(len(self.students))
        for row, student_info in enumerate(self.students):
            self.setup_table_row(row, student_info)

    # 表格行定义
    def setup_table_row(self, row, student_info):
        check_box = QCheckBox()
        self.table_widget.setCellWidget(row, 0, check_box) # 设置第一列为复选框
        # 赋值数据列
        for col, key in enumerate(self.column_lis):
            if key == 'gender':
                value = "男" if student_info.get(key) == 1 else "女"
            else:
                value = student_info.get(key, "") # 不存在赋值空

            # 单元格赋值
            item = QTableWidgetItem(str(value))
            self.table_widget.setItem(row, col+1, item)



if __name__ == '__main__':
    app = QApplication([])

    w = StudentInterface()

    sys.exit(app.exec())
