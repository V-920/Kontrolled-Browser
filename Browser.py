import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        navbar = QToolBar()
        self.addToolBar(navbar)
        homebutton = QAction('Home',self)
        homebutton.triggered.connect(self.navigate_home)
        navbar.addAction(homebutton)
        
        reloadbutton = QAction('Reload',self)
        reloadbutton.triggered.connect(self.browser.reload)
        navbar.addAction(reloadbutton)
        
        backbutton = QAction('Back',self)
        backbutton.triggered.connect(self.browser.back)
        navbar.addAction(backbutton)
        
        forwardbutton = QAction('Forward',self)
        forwardbutton.triggered.connect(self.browser.forward)
        navbar.addAction(forwardbutton)
        
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigatetourl)
        navbar.addWidget(self.urlbar)
        self.browser.urlChanged.connect(self.updateurl)
    def updateurl(self,q):
        self.urlbar.setText(q.toString())
        
        
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))
    def navigatetourl(self):
        url = 'https://' + self.urlbar.text()
        self.browser.setUrl(QUrl(url))
app = QApplication(sys.argv)
QApplication.setApplicationName("Kontrolled Browser")
window = MainWindow()
app.exec_() 