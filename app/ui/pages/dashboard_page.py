from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QHBoxLayout

from app.ui.widgets.info_card import InfoCard


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        card_layout = QHBoxLayout()

        card_layout.addWidget(
            InfoCard("신규 쇼츠", "0")
        )

        card_layout.addWidget(
            InfoCard("분석 완료", "0")
        )

        card_layout.addWidget(
            InfoCard("바이럴 후보", "0")
        )

        main_layout.addLayout(card_layout)

        self.setLayout(main_layout)