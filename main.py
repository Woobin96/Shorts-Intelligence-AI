# import sys

# from PySide6.QtWidgets import QApplication
# from PySide6.QtWidgets import QWidget


# def main():
#     app = QApplication(sys.argv)

#     window = QWidget()
#     window.setWindowTitle("Shorts Intelligence AI")
#     window.resize(800, 500)
#     window.show()

#     sys.exit(app.exec())


# if __name__ == "__main__":
#     main()

import sys

from PySide6.QtWidgets import QApplication

from app.ui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()