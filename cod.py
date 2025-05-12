import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # ایجاد یک شیء QLabel برای نمایش عکس
        self.label = QLabel(self)

        # بارگذاری عکس از فایل
        pixmap = QPixmap('./assets/bg.png')  

        # تنظیم عکس در QLabel
        self.label.setPixmap(pixmap)

        # تغییر اندازه QLabel به اندازه عکس
        self.label.resize(pixmap.width(), pixmap.height())

        # ایجاد یک طرح‌بندی عمودی و افزودن QLabel به آن
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)

        # تنظیم طرح‌بندی روی پنجره اصلی
        self.setLayout(vbox)

        # تنظیم عنوان پنجره
        self.setWindowTitle('نمایش عکس')

        # نمایش پنجره
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



class CenteredImageWindow(QWidget):
    def init(self):
        super().init()

        self.setWindowTitle
        self.setGeometry(100, 100, 500, 400)

        # لود عکس
        pixmap = QPixmap("./assets/map/map-1.png")  # اسم عکس و مسیرش

        # ساخت لیبل و تنظیم عکس
        label = QLabel()
        label.setPixmap(pixmap)
        label.setScaledContents(True)