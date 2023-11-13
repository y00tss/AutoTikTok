import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QGridLayout, QVBoxLayout
from AI.cv import load_video


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QPushButton Widget')
        self.setGeometry(200, 150, 1200, 860)

        # TIKTOK
        button_tiktok = QPushButton('Open TikTok', self)
        button_tiktok.move(0, 100)
        button_tiktok.clicked.connect(load_video)

        # INSTAGRAM
        button_instagram = QPushButton('Open Instagram', self)
        button_instagram.move(500, 0)

        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(button_tiktok)
        layout.addWidget(button_instagram)
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())
