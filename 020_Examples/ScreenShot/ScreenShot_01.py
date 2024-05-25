import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,  QMessageBox
from PySide6.QtGui import QPixmap, QPainter

class ScreenshotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Screenshot App")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("This is a screenshot application.")
        layout.addWidget(self.label)

        self.button = QPushButton("Take Screenshot")
        self.button.clicked.connect(self.take_screenshot)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def take_screenshot(self):
        # Get the geometry of the screen
        screen_geometry = QApplication.primaryScreen().geometry()

        # Create a pixmap with the size of the screen
        pixmap = QPixmap(screen_geometry.size())

        # Grab the screen and save it to the pixmap
        pixmap.grabWindow(QApplication.desktop().winId(), screen_geometry.x(), screen_geometry.y(), screen_geometry.width(), screen_geometry.height())

        # Save the screenshot to a file
        if pixmap.save("screenshot.png"):
            QMessageBox.information(self, "Success", "Screenshot saved as 'screenshot.png'")
        else:
            QMessageBox.warning(self, "Error", "Failed to save screenshot.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScreenshotApp()
    window.show()
    sys.exit(app.exec())