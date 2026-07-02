from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class InfoCard(QWidget):
    def __init__(self, title: str, value: str):
        super().__init__()

        self.setFixedSize(240, 130)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 18, 20, 18)
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("""
            color: #6B7280;
            font-size: 15px;
            font-weight: 600;
        """)

        value_label = QLabel(value)
        value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        value_label.setStyleSheet("""
            color: #111827;
            font-size: 34px;
            font-weight: 800;
        """)

        layout.addWidget(title_label)
        layout.addWidget(value_label)

        self.setLayout(layout)

        self.setStyleSheet("""
            InfoCard {
                background: #FFFFFF;
                border: 1px solid #E5E7EB;
                border-radius: 18px;
            }

            InfoCard:hover {
                border: 1px solid #60A5FA;
                background: #F9FAFB;
            }
        """)