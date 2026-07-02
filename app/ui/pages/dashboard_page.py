from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from app.ui.widgets.recent_shorts_item import RecentShortsItem
from app.ui.widgets.info_card import InfoCard
from PySide6.QtWidgets import QFrame

class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(35, 25, 35, 35)
        main_layout.setSpacing(25)

        card_layout = QHBoxLayout()
        card_layout.setSpacing(20)

        card_layout.addWidget(InfoCard("신규 쇼츠", "0"))
        card_layout.addWidget(InfoCard("분석 완료", "0"))
        card_layout.addWidget(InfoCard("바이럴 후보", "0"))
        card_layout.addStretch()

        recent_title = QLabel("최근 발견한 쇼츠")
        recent_title.setStyleSheet("""
            color: #111827;
            font-size: 20px;
            font-weight: 800;
        """)
        recent_box = QFrame()
        recent_box.setMinimumHeight(220)
        recent_box.setStyleSheet("""
            QFrame {
                background: #FFFFFF;
                border: 1px solid #E5E7EB;
                border-radius: 18px;
            }
        """)

        recent_layout = QVBoxLayout()
        recent_layout.setContentsMargins(12, 12, 12, 12)
        recent_layout.setSpacing(0)

        recent_layout.addWidget(RecentShortsItem("MrBeast", "NEW", "+521K", "3분 전"))
        recent_layout.addWidget(RecentShortsItem("Daily Dose", "HOT", "+182K", "8분 전"))
        recent_layout.addWidget(RecentShortsItem("ESPN", "HOT", "+95K", "12분 전"))
        recent_layout.addWidget(RecentShortsItem("NASA", "NEW", "+66K", "20분 전"))
        recent_layout.addStretch()

        recent_box.setLayout(recent_layout)

        # recent_box = QLabel(
        #     "아직 발견한 쇼츠가 없습니다.\n\n"
        #     "나중에 YouTube API가 연결되면 여기에 신규 쇼츠가 표시됩니다."
        # )

        
        # recent_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # recent_box.setMinimumHeight(220)
        # recent_box.setStyleSheet("""
        #     QLabel {
        #         color: #6B7280;
        #         background: #FFFFFF;
        #         border: 1px solid #E5E7EB;
        #         border-radius: 18px;
        #         font-size: 14px;
        #     }
        # """)

        main_layout.addLayout(card_layout)
        main_layout.addWidget(recent_title)
        main_layout.addWidget(recent_box)
        main_layout.addStretch()

        self.setLayout(main_layout)

        self.setStyleSheet("""
            DashboardPage {
                background: #F3F4F6;
            }
        """)