import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt

class ImageWindow(QWidget):
    def __init__(self, bg_path, overlay_path):
        super().__init__()
        self.setWindowTitle('Image Overlay')
        self.setGeometry(100, 100, 800, 600)

        self.bg_path = bg_path
        self.overlay_path = overlay_path
        self.label = QLabel(self)

        self.load_images()
        self.show()

    def load_images(self):
        try:
            bg_pixmap = QPixmap(self.bg_path)
            overlay_pixmap = QPixmap(self.overlay_path)

            if bg_pixmap.isNull() or overlay_pixmap.isNull():
                raise FileNotFoundError("One or both images not found.")

            # Create a new pixmap for the background with the specified color
            combined_pixmap = QPixmap(bg_pixmap.size())
            creamy_orange = QColor(240, 180, 120)  # Creamy Orange color
            combined_pixmap.fill(creamy_orange)

            painter = QPainter(combined_pixmap)
            painter.drawPixmap(0, 0, bg_pixmap)

            x_offset = 100
            y_offset = 50
            painter.drawPixmap(x_offset, y_offset, overlay_pixmap)
            painter.end()

            self.label.setPixmap(combined_pixmap)
            self.label.setScaledContents(True)

            vbox = QVBoxLayout(self)
            vbox.addWidget(self.label)
            self.setLayout(vbox)
        except FileNotFoundError as e:
            error_label = QLabel(f"Error: {e}", self)
            vbox = QVBoxLayout(self)
            vbox.addWidget(error_label)
            self.setLayout(vbox)


    def resizeEvent(self, event):
        if self.label:
            self.label.setPixmap(self.label.pixmap())
        QWidget.resizeEvent(self, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    bg_image_path = './assets/bg.png'
    overlay_image_path = './assets/map/map-1.png'
    window = ImageWindow(bg_image_path, overlay_image_path)
    sys.exit(app.exec_())
