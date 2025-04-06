"""
添加和删除学生的基类
"""
from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QGridLayout, QLabel

from qfluentwidgets import MessageBoxBase, LineEdit, ComboBox, StrongBodyLabel, SubtitleLabel, InfoBar

from database.classes_db import ClassDB


class BaseStudentDialog(MessageBoxBase):
    def __init__(self, tile, parent=None):
        super().__init__(parent)
        self.tile = tile
        self.setup_ui()

    def setup_ui(self):
        self.titleLabel = SubtitleLabel(self.tile, self)
        self.viewLayout.addWidget(self.titleLabel, alignment=Qt.AlignmentFlag.AlignCenter)

        # 创建一个布局
        grid_layout = QGridLayout()
        # 添加到父布局
        self.viewLayout.addLayout(grid_layout)

        # 创建各字段
        self.nameInput = LineEdit(self)
        self.numberInput = LineEdit(self)
        self.genderComb = ComboBox(self) # 下拉菜单
        self.genderComb.addItems(["男", "女"])
        self.classComb = ComboBox(self)
        self.load_classes()
        self.chineseInput = LineEdit(self)
        self.mathInput = LineEdit(self)
        self.englishInput = LineEdit(self)

        # 添加字段到网格布局
        fields = [
            ("姓名", self.nameInput),
            ("学号", self.numberInput),
            ("性别", self.genderComb),
            ("班级", self.classComb),
            ("语文", self.chineseInput),
            ("数学", self.mathInput),
            ("英语", self.englishInput),
        ]

        for row, (label_text, widget) in enumerate(fields):
            label = StrongBodyLabel(label_text, self) # 制作label widget
            grid_layout.addWidget(label, row , 0)
            grid_layout.addWidget(widget, row, 1)

        # 设置列拉伸
        grid_layout.setColumnStretch(1, 1)
        grid_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.yesButton.setText("确定")
        self.cancelButton.setText("取消")

        for widget in [self.nameInput,
                       self.numberInput,
                       self.genderComb,
                       self.classComb,
                       self.chineseInput,
                       self.mathInput,
                       self.englishInput]:
            widget.setMinimumWidth(200) # 设置最小宽度
        # 将焦点放在姓名框
        self.nameInput.setFocus()
        # 确定不会自动对焦按钮
        self.yesButton.setDefault(False)
        self.cancelButton.setDefault(False)

    def load_classes(self):
        self.classComb.clear() #每次加载前清除
        with ClassDB() as db:
            classes = db.fetch_classes()
        self.classComb.addItem("请选择班级", None)

        for class_info in classes:
            class_id = class_info.get("class_id")
            class_name = class_info.get("class_name")
            self.classComb.addItem(class_name, userData=class_id)
    def accept(self):
        # 验证数据
        error = self._validation()
        if error:
            error_message = "\n".join(error)
            InfoBar.error(title="输入有误", content=error_message, parent=self, duration=3000) # duration为持续时长
            return
        # 验证通过则关闭对话框
        super().accept()

    def _score_validation(self, score):
        if not score.isdigit():
            return False
        return 0<= float(score) <= 100


    def _validation(self):
        errors = []
        if not self.nameInput.text().strip():
            errors.append("姓名不能为空")
        if not self.numberInput.text().strip():
            errors.append("学号不能为空")

        if self.classComb.currentData() is None:
            errors.append("班级不能为空")
        for subject, input_field in [("语文", self.chineseInput),
                               ("数学", self.mathInput),
                               ("英语", self.englishInput)]:
            score = input_field.text().strip()
            if not self._score_validation(score):
                errors.append("请输入一个0-100之间的数字")

        return errors
    def get_student_info(self):
        """获取学生信息"""
        name = self.nameInput.text().strip()
        gender = self.genderComb.currentData()
        number = self.numberInput.text().strip()
        class_id = self.classComb.currentData()
        chinese_score = self.chineseInput.text().strip()
        math_score = self.mathInput.text().strip()
        english_score = self.englishInput.text().strip()

        return {"name": name,
                "gender":1 if gender == "男" else 2,
                "number": number,
                "class_id":class_id,
                "chinese_score": chinese_score,
                "math_score": math_score,
                "english_score": english_score,
                "total_score": float(chinese_score) + float(math_score) + float(english_score)}



class AddStudentDialog(BaseStudentDialog):
    def __init__(self, parent=None):
        super().__init__("添加学生", parent)
        self.yesButton.setText("添加")

class UpdateStudentDialog(BaseStudentDialog):
    def __init__(self, parent=None):
        super().__init__("编辑学生", parent)
        self.yesButton.setText("修改")
    def set_student_info(self, info):
        self.nameInput.setText(info["student_name"])
        self.numberInput.setText(info["student_number"])
        self.genderCombo.setCurrentData(info["gender"])

        #
