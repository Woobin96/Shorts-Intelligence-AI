from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(180)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(15, 20, 15, 20)
        layout.setSpacing(10)

        title = QLabel("🚀 SIA")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 20px;
            }
        """)

        layout.addWidget(title)

        menus = [
            "🏠 Dashboard",
            "📺 Monitor",
            "📈 Trending",
            "🤖 AI Studio",
            "🎙️ Dubbing",
            "📂 Downloads",
            "⚙ Settings",
        ]

        for menu in menus:
            button = QPushButton(menu)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.setStyleSheet("""
                QPushButton {
                    background: transparent;
                    color: #D4D4D4;
                    border: none;
                    text-align: left;
                    padding: 10px;
                    font-size: 14px;
                    border-radius: 8px;
                }

                QPushButton:hover {
                    background: #2D2D30;
                    color: #FFFFFF;
                }
            """)
            layout.addWidget(button)

        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget {
                background: #181818;
            }
        """)