from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout


class InfoCard(QWidget):

    def __init__(self, title: str, value: str):
        super().__init__()

        self.setFixedSize(220, 120)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_font = QFont()
        title_font.setPointSize(11)
        self.title.setFont(title_font)

        self.value = QLabel(value)
        self.value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        value_font = QFont()
        value_font.setPointSize(24)
        value_font.setBold(True)
        self.value.setFont(value_font)

        layout.addWidget(self.title)
        layout.addWidget(self.value)

        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget{
                background:#F7F7F7;
                border:1px solid #DDDDDD;
                border-radius:15px;
            }

            QLabel{
                background:transparent;
                border:none;
            }
        """)