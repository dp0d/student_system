from PyQt6.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import PushButton, setCustomStyleSheet

from utils.custom_style import UPDATE_BUTTON_STYLE, DELETE_BUTTON_STYLE


def create_action_widget(update_callback, delete_callback):
    # 编辑一个widget容器
    widget = QWidget()
    layout = QHBoxLayout(widget)
    layout.setContentsMargins(0, 0, 0, 0)  # 设置边距
    edit_button = PushButton("编辑")
    setCustomStyleSheet(edit_button, UPDATE_BUTTON_STYLE, UPDATE_BUTTON_STYLE)
    edit_button.clicked.connect(update_callback)
    delete_button = PushButton("删除")
    setCustomStyleSheet(delete_button, DELETE_BUTTON_STYLE, DELETE_BUTTON_STYLE)
    delete_button.clicked.connect(delete_callback)
    layout.addWidget(edit_button)
    layout.addWidget(delete_button)

    return widget