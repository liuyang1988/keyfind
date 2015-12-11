# -*- coding: utf-8 -*-

"""
Module implementing KeyFind.
"""

from PyQt5.QtCore import pyqtSlot, QModelIndex
from PyQt5.QtWidgets import QDialog
#pp
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog

from Ui_keyfind import Ui_Dialog


class KeyFind(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(KeyFind, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_fileopen_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        files, ok1 = QFileDialog.getOpenFileNames(self, 
                                 "search files", 
                                 "C:/Python34",
                                 "All files(*);;Text files(*.txt)")
        print (files)
        #将选中的文件名加入listWidget中
        self.listWidget_filenames.addItems(files)
        
     
        
     # 对选择的文件进行关键字查找，关键字在程序中定义好。12092015
    @pyqtSlot()
    def on_pushButton_searchsinglefile_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        print("now seaech the selected file by keyword")
        row = self.listWidget_filenames.currentRow()
        currentfile = self.listWidget_filenames.item(row).text()
        print (currentfile)   
       #打开currentfile,进行关键字查找
        import re
        f = open(currentfile,'r')
        keyword1= re.compile('ddd[a-e] \d{4}')
        keyword2 = re.compile('\.\S{6}[AS]')
        
        #进行正则表达式的匹配
        for line in f:
            rs1 = keyword1.findall(line)
            if rs1:
                print(rs1)
                self.listWidget_sr_show.addItems(rs1)
                
                
            rs2 = keyword2.findall(line)
            if rs2:
                print(rs2)
                self.listWidget_sr_show.addItems(rs2)
           

 
    @pyqtSlot()       
    def on_pushButton_searchmiltfiles_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        #pp 正则表达式，或许可以移到init中
#        import re
#        keyword1= re.compile('ddd[a-e] \d{4}')
#        keyword2 = re.compile('\.\S{6}[AS]')
        
        filenames = self.listWidget_filenames.selectedIndexes()
        for f in filenames:
            print("i am here")
            print(f.data())
            
 
#        row = self.listWidget_filenames.currentRow()
#        currentfile = self.listWidget_filenames.item(row).text()
#        print (filenames)
        
#        print (filenames)
#        for f  in open(filenames, 'r'):
#            for line in f:
#                rs1 = keyword1.findall(line)
#                if rs1:
#                  print(rs1)
#                self.listWidget_sr_show.addItems(rs1)
#                
#                
#                rs2 = keyword2.findall(line)
#                if rs2:
#                   print(rs2)
#                   self.listWidget_sr_show.addItems(rs2) 
        
    
    @pyqtSlot()
    def on_pushButton_openselectfile_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        print("now open the selected file in textedit")
        row = self.listWidget_filenames.currentRow()
        currentfile = self.listWidget_filenames.item(row).text()
        print (currentfile)   
       #打开currentfile,进行关键字查找
        file = QtCore.QFile(currentfile)
        if not file.open(QtCore.QIODevice.ReadOnly):
            QtGui.QMessageBox.information(None, 'info', file.errorString())
        stream = QtCore.QTextStream(file)
        self.textEdit_sr_show.setText(stream.readAll())
        
    @pyqtSlot()
    def on_pushButton_version_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.label_status.setText("current version 1.0")
       
        
#add by pp        to show windows and run
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = KeyFind()
    dlg.show()
    sys.exit(app.exec_())
    
 
