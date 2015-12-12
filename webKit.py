#encoding = utf-8
__author__ = 'Andy'
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView

class Brower(QWebView):

    def __init__(self):
        QWebView.__init__(self)
        self.loadFinished.connect(self._result_available)

    def _result_available(self, ok):
        frame = self.page().mainFrame()

        dom = unicode(frame.toHtml()).encode("utf-8")
        parse(dom)

def pase(dom):
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #view = QWebView()
    view = Brower()
    url = "http://www.baidu.com"
    view.load(QUrl(url))
    view.show()
    app.exec_()
