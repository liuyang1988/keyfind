# -*- coding: utf-8 -*-

"""
Module implementing KeyFind.
"""

from PyQt5.QtCore import pyqtSlot, QModelIndex
from PyQt5.QtWidgets import QDialog
#pp
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
        
        
    @pyqtSlot()
    def on_pushButton_keyword3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_keyword1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_keyword2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_version_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.label_status.setText("curren version 1.0")
        
    @pyqtSlot(QModelIndex)
    def on_listWidget_filenames_clicked(self, index):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        print ("hello")
        row = self.listWidget_filenames.currentRow()
        currentfile = self.listWidget_filenames.item(row).text()
        print (currentfile)
        
        
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = KeyFind()
    dlg.show()
    sys.exit(app.exec_())
    
   
