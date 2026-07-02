from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout


class RecentShortsItem(QWidget):
    def __init__(self, channel: str, badge: str, growth: str, time: str):
        super().__init__()

        layout = QHBoxLayout()
        layout.setContentsMargins(18, 12, 18, 12)

        channel_label = QLabel(channel)
        badge_label = QLabel(badge)
        growth_label = QLabel(growth)
        time_label = QLabel(time)

        channel_label.setStyleSheet("font-size: 14px; font-weight: 700; color: #111827;")
        badge_label.setStyleSheet("font-size: 12px; font-weight: 800; color: #2563EB;")
        growth_label.setStyleSheet("font-size: 14px; font-weight: 700; color: #10B981;")
        time_label.setStyleSheet("font-size: 13px; color: #6B7280;")

        layout.addWidget(channel_label)
        layout.addStretch()
        layout.addWidget(badge_label)
        layout.addSpacing(20)
        layout.addWidget(growth_label)
        layout.addSpacing(20)
        layout.addWidget(time_label)

        self.setLayout(layout)

        self.setStyleSheet("""
            RecentShortsItem {
                background: #FFFFFF;
                border-bottom: 1px solid #E5E7EB;
            }
        """)