from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(220)

        layout = QVBoxLayout()
        layout.setContentsMargins(18, 22, 18, 18)
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        logo = QLabel("🚀  Shorts AI")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-size: 20px;
                font-weight: 800;
                padding: 14px;
                background: #111827;
                border-radius: 14px;
            }
        """)

        layout.addWidget(logo)
        layout.addSpacing(18)

        menus = [
            ("🏠", "Dashboard", True),
            ("📺", "Monitor", False),
            ("📈", "Trending", False),
            ("🤖", "AI Studio", False),
            ("🌎", "Translation", False),
            ("🎙️", "Dubbing", False),
            ("📂", "Downloads", False),
            ("⚙", "Settings", False),
        ]

        for icon, text, active in menus:
            button = QPushButton(f"{icon}   {text}")
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.setFixedHeight(44)

            if active:
                button.setStyleSheet("""
                    QPushButton {
                        background: #2563EB;
                        color: #FFFFFF;
                        border: none;
                        border-radius: 12px;
                        text-align: left;
                        padding-left: 16px;
                        font-size: 14px;
                        font-weight: 700;
                    }
                """)
            else:
                button.setStyleSheet("""
                    QPushButton {
                        background: transparent;
                        color: #9CA3AF;
                        border: none;
                        border-radius: 12px;
                        text-align: left;
                        padding-left: 16px;
                        font-size: 14px;
                        font-weight: 600;
                    }

                    QPushButton:hover {
                        background: #1F2937;
                        color: #FFFFFF;
                    }
                """)

            layout.addWidget(button)

        layout.addStretch()

        status = QLabel("● GitHub Connected\nv0.1.0")
        status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        status.setStyleSheet("""
            QLabel {
                color: #10B981;
                font-size: 12px;
                padding: 12px;
                background: #111827;
                border-radius: 12px;
            }
        """)

        layout.addWidget(status)

        self.setLayout(layout)

        self.setStyleSheet("""
            Sidebar {
                background: #0F172A;
            }
        """)