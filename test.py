import sys
from PyQt6.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        # *args: 任意数量的参数
        # **kwargs: 任意数量的关键字参数(如windowTitle:"Hello, World!")
        super().__init__(*args, **kwargs)
        self.setWindowTitle("hello, world!")
        self.show()

if __name__ == '__main__':
    # 创建一个应用
    app = QApplication([])
    w = MainWindow()
    sys.exit(app.exec()) # 窗口执行完毕后则退出这个程序