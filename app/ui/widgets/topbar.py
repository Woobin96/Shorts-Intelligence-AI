from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton


class TopBar(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(70)

        layout = QHBoxLayout()
        layout.setContentsMargins(25, 10, 25, 10)

        title = QLabel("Dashboard")
        title.setStyleSheet("""
            QLabel {
                color: #111111;
                font-size: 24px;
                font-weight: bold;
            }
        """)

        spacer = QLabel("")

        alert_button = QPushButton("🔔")
        theme_button = QPushButton("🌙")
        setting_button = QPushButton("⚙")

        for button in [alert_button, theme_button, setting_button]:
            button.setFixedSize(40, 40)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.setStyleSheet("""
                QPushButton {
                    background: #F3F4F6;
                    border: none;
                    border-radius: 10px;
                    font-size: 18px;
                }

                QPushButton:hover {
                    background: #E5E7EB;
                }
            """)

        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(alert_button)
        layout.addWidget(theme_button)
        layout.addWidget(setting_button)

        self.setLayout(layout)