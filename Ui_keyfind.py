# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python34\eg\keyfind\keyfind.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(572, 345)
        Dialog.setSizeGripEnabled(True)
        self.pushButton_fileopen = QtWidgets.QPushButton(Dialog)
        self.pushButton_fileopen.setGeometry(QtCore.QRect(30, 50, 75, 23))
        self.pushButton_fileopen.setObjectName("pushButton_fileopen")
        self.pushButton_keyword3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_keyword3.setGeometry(QtCore.QRect(400, 50, 75, 23))
        self.pushButton_keyword3.setObjectName("pushButton_keyword3")
        self.pushButton_keyword1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_keyword1.setGeometry(QtCore.QRect(230, 50, 75, 23))
        self.pushButton_keyword1.setObjectName("pushButton_keyword1")
        self.pushButton_keyword2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_keyword2.setGeometry(QtCore.QRect(320, 50, 75, 23))
        self.pushButton_keyword2.setObjectName("pushButton_keyword2")
        self.pushButton_version = QtWidgets.QPushButton(Dialog)
        self.pushButton_version.setGeometry(QtCore.QRect(320, 300, 75, 23))
        self.pushButton_version.setObjectName("pushButton_version")
        self.pushButton_close = QtWidgets.QPushButton(Dialog)
        self.pushButton_close.setGeometry(QtCore.QRect(410, 300, 75, 23))
        self.pushButton_close.setObjectName("pushButton_close")
        self.listView_filenames = QtWidgets.QListView(Dialog)
        self.listView_filenames.setGeometry(QtCore.QRect(30, 90, 101, 192))
        self.listView_filenames.setObjectName("listView_filenames")
        self.label_status = QtWidgets.QLabel(Dialog)
        self.label_status.setGeometry(QtCore.QRect(30, 310, 271, 16))
        self.label_status.setObjectName("label_status")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(220, 100, 261, 171))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        self.pushButton_close.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_fileopen.setText(_translate("Dialog", "打开文件"))
        self.pushButton_keyword3.setText(_translate("Dialog", "关键词3"))
        self.pushButton_keyword1.setText(_translate("Dialog", "关键词1"))
        self.pushButton_keyword2.setText(_translate("Dialog", "关键词2"))
        self.pushButton_version.setText(_translate("Dialog", "版本信息"))
        self.pushButton_close.setText(_translate("Dialog", "关闭"))
        self.label_status.setText(_translate("Dialog", "状态栏"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

