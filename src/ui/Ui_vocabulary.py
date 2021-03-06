# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_vocabulary.ui'
#
# Created: Tue Sep  6 14:14:57 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_vocabularyDialog(object):
    def setupUi(self, vocabularyDialog):
        vocabularyDialog.setObjectName("vocabularyDialog")
        vocabularyDialog.resize(800, 230)
        vocabularyDialog.setMaximumSize(QtCore.QSize(800, 230))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgs/icons/m_vocabulary.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        vocabularyDialog.setWindowIcon(icon)
        self.label = QtGui.QLabel(vocabularyDialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 811, 311))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/imgs/icons/background.png"))
        self.label.setObjectName("label")
        self.groupBox = QtGui.QGroupBox(vocabularyDialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 800, 230))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(2, 0, 2, 2)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.intoLabel = QtGui.QLabel(self.groupBox)
        self.intoLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.intoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.intoLabel.setObjectName("intoLabel")
        self.gridLayout.addWidget(self.intoLabel, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.harf1 = QtGui.QLabel(self.groupBox)
        self.harf1.setMinimumSize(QtCore.QSize(0, 100))
        self.harf1.setText("")
        self.harf1.setObjectName("harf1")
        self.horizontalLayout.addWidget(self.harf1)
        self.harf2 = QtGui.QLabel(self.groupBox)
        self.harf2.setMinimumSize(QtCore.QSize(0, 100))
        self.harf2.setText("")
        self.harf2.setObjectName("harf2")
        self.horizontalLayout.addWidget(self.harf2)
        self.harf3 = QtGui.QLabel(self.groupBox)
        self.harf3.setMinimumSize(QtCore.QSize(0, 100))
        self.harf3.setText("")
        self.harf3.setObjectName("harf3")
        self.horizontalLayout.addWidget(self.harf3)
        self.harf4 = QtGui.QLabel(self.groupBox)
        self.harf4.setMinimumSize(QtCore.QSize(0, 100))
        self.harf4.setText("")
        self.harf4.setObjectName("harf4")
        self.horizontalLayout.addWidget(self.harf4)
        self.harf5 = QtGui.QLabel(self.groupBox)
        self.harf5.setMinimumSize(QtCore.QSize(0, 100))
        self.harf5.setText("")
        self.harf5.setObjectName("harf5")
        self.horizontalLayout.addWidget(self.harf5)
        self.harf6 = QtGui.QLabel(self.groupBox)
        self.harf6.setMinimumSize(QtCore.QSize(0, 100))
        self.harf6.setText("")
        self.harf6.setObjectName("harf6")
        self.horizontalLayout.addWidget(self.harf6)
        self.harf7 = QtGui.QLabel(self.groupBox)
        self.harf7.setMinimumSize(QtCore.QSize(0, 100))
        self.harf7.setText("")
        self.harf7.setObjectName("harf7")
        self.horizontalLayout.addWidget(self.harf7)
        self.harf8 = QtGui.QLabel(self.groupBox)
        self.harf8.setMinimumSize(QtCore.QSize(0, 100))
        self.harf8.setText("")
        self.harf8.setObjectName("harf8")
        self.horizontalLayout.addWidget(self.harf8)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.romanizedLabel = QtGui.QLabel(self.groupBox)
        self.romanizedLabel.setObjectName("romanizedLabel")
        self.horizontalLayout_3.addWidget(self.romanizedLabel)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(12)
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cevap1Button = QtGui.QPushButton(self.groupBox)
        self.cevap1Button.setMinimumSize(QtCore.QSize(220, 30))
        self.cevap1Button.setObjectName("cevap1Button")
        self.gridLayout_3.addWidget(self.cevap1Button, 0, 1, 1, 1)
        self.cevap3Button = QtGui.QPushButton(self.groupBox)
        self.cevap3Button.setMinimumSize(QtCore.QSize(220, 30))
        self.cevap3Button.setObjectName("cevap3Button")
        self.gridLayout_3.addWidget(self.cevap3Button, 2, 1, 1, 1)
        self.cevap2Button = QtGui.QPushButton(self.groupBox)
        self.cevap2Button.setMinimumSize(QtCore.QSize(220, 30))
        self.cevap2Button.setObjectName("cevap2Button")
        self.gridLayout_3.addWidget(self.cevap2Button, 0, 2, 1, 1)
        self.cevap4Button = QtGui.QPushButton(self.groupBox)
        self.cevap4Button.setMinimumSize(QtCore.QSize(220, 30))
        self.cevap4Button.setObjectName("cevap4Button")
        self.gridLayout_3.addWidget(self.cevap4Button, 2, 2, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 3, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 3, 0, 1, 1)

        self.retranslateUi(vocabularyDialog)
        QtCore.QMetaObject.connectSlotsByName(vocabularyDialog)

    def retranslateUi(self, vocabularyDialog):
        vocabularyDialog.setWindowTitle(QtGui.QApplication.translate("vocabularyDialog", "Vocabulary Test [under-development]", None, QtGui.QApplication.UnicodeUTF8))
        self.intoLabel.setText(QtGui.QApplication.translate("vocabularyDialog", "What Does This Word Means", None, QtGui.QApplication.UnicodeUTF8))
        self.romanizedLabel.setText(QtGui.QApplication.translate("vocabularyDialog", "romanizedLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.cevap1Button.setText(QtGui.QApplication.translate("vocabularyDialog", "answer1", None, QtGui.QApplication.UnicodeUTF8))
        self.cevap3Button.setText(QtGui.QApplication.translate("vocabularyDialog", "answer3", None, QtGui.QApplication.UnicodeUTF8))
        self.cevap2Button.setText(QtGui.QApplication.translate("vocabularyDialog", "answer2", None, QtGui.QApplication.UnicodeUTF8))
        self.cevap4Button.setText(QtGui.QApplication.translate("vocabularyDialog", "answer4", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
