from PyQt5.QtWidgets import *
from query import Kfc_data
from view_win import View

class Admin(QWidget):
     def __init__(self,adminn):
          super().__init__()

          self.adwin = adminn

          self.view_win = View(self)

          self.ttt = Kfc_data()

          self.setFixedSize(520,620)
          self.setStyleSheet("font-size:20px")

          self.h_btn_lyt = QHBoxLayout()
          self.v_main_lyt = QVBoxLayout()

          self.name_edit = QLineEdit()
          self.name_edit.setPlaceholderText("Nomi...")
          self.price_edit = QLineEdit()
          self.price_edit.setPlaceholderText("Narxi...")
          self.sale_edit = QLineEdit()
          self.sale_edit.setPlaceholderText("Soni...")

          self.btn_wiu = QPushButton("Next",clicked = self.wiu_data)
          self.btn_wiu.setFixedSize(100,40)
          self.btn_wiu.setStyleSheet("background:red;color:white")
          self.btn_submit = QPushButton("Submit",clicked = self.submit)
          self.btn_submit.setFixedSize(100,40)
          self.btn_submit.setStyleSheet("background:red;color:white")
          self.btn_back = QPushButton("Exit",clicked=self.back)
          self.btn_back.setFixedSize(100,40)
          self.btn_back.setStyleSheet("background:red;color:white")

          self.h_btn_lyt.addWidget(self.btn_back)
          self.h_btn_lyt.addWidget(self.btn_submit)
          self.h_btn_lyt.addWidget(self.btn_wiu)

          self.lts = [self.name_edit, 
                      self.price_edit, 
                      self.sale_edit]
          
          for i in self.lts:
               i.setFixedSize(500,70)
               self.v_main_lyt.addWidget(i)
          self.v_main_lyt.addLayout(self.h_btn_lyt)

          self.setLayout(self.v_main_lyt)

     def wiu_data(self):
          self.hide()
          self.view_win.show()
          
     def submit(self):
          try:
               self.ttt.insertData([i.text() for i in self.lts]) 
               QMessageBox.information(self,"Ajoyib","Malumotlar muvoffaqiyatli joylandi")
               [i.clear() for i in self.lts]
          except:
               QMessageBox.critical(self,"Xatolik","Maydonni to'liq to'ldiring!!!")
     def back(self):
          self.hide()
          self.adwin.show()






