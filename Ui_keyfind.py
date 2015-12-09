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
        Dialog.resize(800, 457)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.pushButton_fileopen = QtWidgets.QPushButton(Dialog)
        self.pushButton_fileopen.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton_fileopen.setObjectName("pushButton_fileopen")
        self.pushButton_openselectfile = QtWidgets.QPushButton(Dialog)
        self.pushButton_openselectfile.setGeometry(QtCore.QRect(300, 240, 91, 23))
        self.pushButton_openselectfile.setObjectName("pushButton_openselectfile")
        self.pushButton_searchsinglefile = QtWidgets.QPushButton(Dialog)
        self.pushButton_searchsinglefile.setGeometry(QtCore.QRect(300, 100, 91, 23))
        self.pushButton_searchsinglefile.setObjectName("pushButton_searchsinglefile")
        self.pushButton_searchmiltfiles = QtWidgets.QPushButton(Dialog)
        self.pushButton_searchmiltfiles.setGeometry(QtCore.QRect(300, 140, 91, 23))
        self.pushButton_searchmiltfiles.setObjectName("pushButton_searchmiltfiles")
        self.pushButton_version = QtWidgets.QPushButton(Dialog)
        self.pushButton_version.setGeometry(QtCore.QRect(630, 430, 75, 23))
        self.pushButton_version.setObjectName("pushButton_version")
        self.pushButton_close = QtWidgets.QPushButton(Dialog)
        self.pushButton_close.setGeometry(QtCore.QRect(711, 430, 75, 23))
        self.pushButton_close.setObjectName("pushButton_close")
        self.label_status = QtWidgets.QLabel(Dialog)
        self.label_status.setGeometry(QtCore.QRect(10, 430, 491, 16))
        self.label_status.setObjectName("label_status")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(400, 50, 271, 171))
        self.textEdit.setObjectName("textEdit")
        self.listWidget_filenames = QtWidgets.QListWidget(Dialog)
        self.listWidget_filenames.setGeometry(QtCore.QRect(10, 50, 281, 341))
        self.listWidget_filenames.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget_filenames.setObjectName("listWidget_filenames")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(400, 240, 271, 151))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Dialog)
        self.pushButton_close.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_fileopen.setText(_translate("Dialog", "打开文件"))
        self.pushButton_openselectfile.setText(_translate("Dialog", "打开选中文件"))
        self.pushButton_searchsinglefile.setText(_translate("Dialog", "查找单个文件"))
        self.pushButton_searchmiltfiles.setText(_translate("Dialog", "查找多个文件"))
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

