from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout

from app.ui.pages.dashboard_page import DashboardPage
from app.ui.widgets.sidebar import Sidebar
from app.ui.widgets.topbar import TopBar


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shorts Intelligence AI")
        self.resize(1200, 760)

        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        sidebar = Sidebar()

        content_widget = QWidget()
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        topbar = TopBar()
        dashboard = DashboardPage()

        content_layout.addWidget(topbar)
        content_layout.addWidget(dashboard)

        content_widget.setLayout(content_layout)

        main_layout.addWidget(sidebar)
        main_layout.addWidget(content_widget)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)