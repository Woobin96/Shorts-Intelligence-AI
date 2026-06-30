from PySide6.QtWidgets import QMainWindow

from app.ui.pages.dashboard_page import DashboardPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shorts Intelligence AI")
        self.resize(900, 600)

        dashboard = DashboardPage()

        self.setCentralWidget(dashboard)