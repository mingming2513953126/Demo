#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from PyQt4 import QtCore, QtGui

class MyWidget(QtGui.QWidget): #实现自定义的窗口部件
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setFixedSize(200, 120)

        self.quit = QtGui.QPushButton("Quit", self)
        self.quit.setGeometry(62, 40, 75, 30)
        self.quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

        #关联信号
        self.connect(self.quit, QtCore.SIGNAL("clicked()"),
                     QtGui.qApp, QtCore.SLOT("quit()"))

app = QtGui.QApplication(sys.argv)

widget = MyWidget()
widget.show()

sys.exit(app.exec_())