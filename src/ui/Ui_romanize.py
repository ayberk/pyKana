# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_romanize.ui'
#
# Created: Mon Aug 22 00:04:09 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_romanizeDialog(object):
    def setupUi(self, romanizeDialog):
        romanizeDialog.setObjectName("romanizeDialog")
        romanizeDialog.resize(700, 200)
        romanizeDialog.setMinimumSize(QtCore.QSize(700, 200))
        romanizeDialog.setMaximumSize(QtCore.QSize(700, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgs/icons/m_romanize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        romanizeDialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(romanizeDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.harf1 = QtGui.QLabel(romanizeDialog)
        self.harf1.setText("")
        self.harf1.setObjectName("harf1")
        self.horizontalLayout.addWidget(self.harf1)
        self.harf2 = QtGui.QLabel(romanizeDialog)
        self.harf2.setText("")
        self.harf2.setObjectName("harf2")
        self.horizontalLayout.addWidget(self.harf2)
        self.harf3 = QtGui.QLabel(romanizeDialog)
        self.harf3.setText("")
        self.harf3.setObjectName("harf3")
        self.horizontalLayout.addWidget(self.harf3)
        self.harf4 = QtGui.QLabel(romanizeDialog)
        self.harf4.setText("")
        self.harf4.setObjectName("harf4")
        self.horizontalLayout.addWidget(self.harf4)
        self.harf5 = QtGui.QLabel(romanizeDialog)
        self.harf5.setText("")
        self.harf5.setObjectName("harf5")
        self.horizontalLayout.addWidget(self.harf5)
        self.harf6 = QtGui.QLabel(romanizeDialog)
        self.harf6.setText("")
        self.harf6.setObjectName("harf6")
        self.horizontalLayout.addWidget(self.harf6)
        self.harf7 = QtGui.QLabel(romanizeDialog)
        self.harf7.setText("")
        self.harf7.setObjectName("harf7")
        self.horizontalLayout.addWidget(self.harf7)
        self.harf8 = QtGui.QLabel(romanizeDialog)
        self.harf8.setText("")
        self.harf8.setObjectName("harf8")
        self.horizontalLayout.addWidget(self.harf8)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.lineEdit = QtGui.QLineEdit(romanizeDialog)
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)
        self.checkButton = QtGui.QPushButton(romanizeDialog)
        self.checkButton.setObjectName("checkButton")
        self.gridLayout.addWidget(self.checkButton, 2, 0, 1, 1)
        self.quitButton = QtGui.QPushButton(romanizeDialog)
        self.quitButton.setObjectName("quitButton")
        self.gridLayout.addWidget(self.quitButton, 2, 1, 1, 1)

        self.retranslateUi(romanizeDialog)
        QtCore.QObject.connect(self.quitButton, QtCore.SIGNAL("clicked()"), romanizeDialog.close)
        QtCore.QMetaObject.connectSlotsByName(romanizeDialog)
        romanizeDialog.setTabOrder(self.lineEdit, self.checkButton)
        romanizeDialog.setTabOrder(self.checkButton, self.quitButton)

    def retranslateUi(self, romanizeDialog):
        romanizeDialog.setWindowTitle(QtGui.QApplication.translate("romanizeDialog", "Romanize The Given Word [under-development]", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("romanizeDialog", "romanize it here and press enter", None, QtGui.QApplication.UnicodeUTF8))
        self.checkButton.setText(QtGui.QApplication.translate("romanizeDialog", "Check", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setText(QtGui.QApplication.translate("romanizeDialog", "Quit", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
