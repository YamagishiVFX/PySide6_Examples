import sys
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QMessageBox
from PySide6.QtGui import QPixmap

class ScreenshotApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Screenshot App')
        self.resize(400, 300)

        self.layout = QVBoxLayout()

        self.screenshot_button = QPushButton('Take Screenshot')
        self.screenshot_button.clicked.connect(self.take_screenshot)
        self.layout.addWidget(self.screenshot_button)

        self.setLayout(self.layout)

    def take_screenshot(self):
        # アクティブウィンドウを取得
        active_window = QApplication.activeWindow()
        if active_window:
            # アクティブウィンドウのスクリーンショットを取得
            screenshot = active_window.grab()
            # スクリーンショットを保存
            if not screenshot.isNull():
                screenshot.save("screenshot.png", "png")
                QMessageBox.information(self, "Screenshot Saved", "Screenshot saved as screenshot.png")
            else:
                QMessageBox.warning(self, "Screenshot Error", "Failed to take screenshot")
        else:
            QMessageBox.warning(self, "No Active Window", "There is no active window")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ScreenshotApp()
    window.show()
    sys.exit(app.exec())