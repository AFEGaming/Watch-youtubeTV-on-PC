import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile


class SimpleBrowser(QMainWindow):
    def __init__(self):
        super(SimpleBrowser, self).__init__()

        # Tarayıcı profili oluşturma ve kullanıcı aracını ayarlama
        profile = QWebEngineProfile.defaultProfile()
        profile.setHttpUserAgent("Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36 DMOST/2.0.0 (; LGE; webOSTV; WEBOS6.3.2 03.34.95; W6_lm21a;)")

        # Tarayıcı bileşeni oluşturma
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.youtube.com/tv"))  # Başlangıç sayfası

        # Ana pencereye tarayıcıyı ekleme
        self.setCentralWidget(self.browser)

        # Pencere ayarları
        self.showMaximized()

    def keyPressEvent(self, event):
        # fn + F11 kombinasyonu ile tam ekran geçişi
        if event.key() == Qt.Key_F11:  # F11 tuşuna basıldığında
            if self.isFullScreen():
                self.setWindowState(self.windowState() & ~Qt.WindowFullScreen)  # Tam ekrandan çık
            else:
                self.setWindowState(self.windowState() | Qt.WindowFullScreen)  # Tam ekran ol

app = QApplication(sys.argv)
QApplication.setApplicationName("Basit Tarayıcı")
window = SimpleBrowser()
app.exec_()
