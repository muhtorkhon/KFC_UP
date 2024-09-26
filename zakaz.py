from PyQt5.QtWidgets import *
from query import *
from view_win import View

class Addmanzil(QWidget):
    def __init__(self,addwin):
        super().__init__()
        self.addv = addwin

        self.view_win = View(self)
        self.taom = Kfc_data()
        self.adress = Manzil()
        self.setFixedSize(520,620)
        self.setStyleSheet("font-size:20px")

        self.lbl = QLabel("")
        self.lbl.setStyleSheet("background:red;color:white;font-size:40px")
        self.lbl.hide()

        self.lbl_sum = QLabel("")
        self.lbl_sum.setStyleSheet("background:red;color:white;font-size:40px")
        self.lbl_sum.hide()

        self.h_btn_lyt = QHBoxLayout()
        self.v_main_lyt = QVBoxLayout()
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Shahar...")
        self.name_edit.hide()
        self.price_edit = QLineEdit()
        self.price_edit.setPlaceholderText("Ko'cha...")
        self.price_edit.hide()
        self.sale_edit = QLineEdit()
        self.sale_edit.setPlaceholderText("Uy...")
        self.sale_edit.hide()
        self.tola_edit = QLineEdit()
        self.tola_edit.setPlaceholderText("To'lov...")
        self.tola_edit.hide()

        self.soni_edit = QLineEdit()
        self.soni_edit.setFixedSize(500,70)
        self.soni_edit.setPlaceholderText("Soni...")

        self.btn_submit = QPushButton("Next",clicked = self.submit)
        self.btn_submit.setFixedSize(100,40)
        self.btn_submit.setStyleSheet("background:red;color:white")
        self.btn_submit.hide()

        self.btn_back = QPushButton("Exit",clicked=self.back)
        self.btn_back.setFixedSize(100,40)
        self.btn_back.setStyleSheet("background:red;color:white")
        self.btn_back.hide()

        self.btn_sum = QPushButton("Summa",clicked=self.summas)
        self.btn_sum.setFixedSize(100,40)
        self.btn_sum.setStyleSheet("background:red;color:white")

        self.lts_manzil = [self.name_edit,
                           self.price_edit,
                           self.sale_edit]

        self.h_btn_lyt.addWidget(self.btn_back)
        self.h_btn_lyt.addWidget(self.btn_submit)
        self.h_btn_lyt.addWidget(self.btn_sum)
        self.lts = [self.name_edit, 
                    self.price_edit, 
                    self.sale_edit]
        self.v_main_lyt.addWidget(self.lbl)
        self.v_main_lyt.addWidget(self.lbl_sum)
        for i in self.lts:
            i.setFixedSize(500,70)
            self.v_main_lyt.addWidget(i)
        self.v_main_lyt.addWidget(self.soni_edit)
        self.v_main_lyt.addWidget(self.tola_edit)
        self.v_main_lyt.addLayout(self.h_btn_lyt)
        self.setLayout(self.v_main_lyt)

    def wiu_data(self):
        self.hide()
        self.view_win.show()
          
    def submit(self):
        self.adress.insertData([i.text() for i in self.lts_manzil])
        try:
            if self.tola_edit.text().isdigit() and float(self.tola_edit.text()) == self.suma:
                QMessageBox.information(self,"Ajoyib","Buyurtma qabul qilindi\n30 daqiqa ichida yetkaziladi")
                self.taom.clousss()
                self.name_edit.clear()
                self.price_edit.clear()
                self.sale_edit.clear()
                self.tola_edit.clear()
            else:
                QMessageBox.critical(self,"Xatolik","To'lovda xatolik bor!!!")
                self.tola_edit.clear()
        except:
             QMessageBox.critical(self,"Xatolik","Maydonni to'liq to'ldiring!!!")
    def back(self):
        self.narx = ""
        self.lbl.clear()
        self.lbl_sum.clear()
        self.hide()
        self.addv.show()
        self.soni_edit.show()
        self.btn_sum.show()
        self.name_edit.hide()
        self.price_edit.hide()
        self.sale_edit.hide()
        self.tola_edit.hide()
        self.btn_submit.hide()
        self.btn_back.hide()
        self.lbl_sum.hide()
        

    def xissob(self,nom,narx):
        self.lbl.setText(f"   {nom}\n\n   {narx}\n\n   Sonini kiriting!!!")
        self.lbl.show()
        self.nom = nom
        self.narx = narx

    def summas(self):
        if self.soni_edit.text().isdigit():
            self.lbl.hide()
            self.suma = float(self.narx) * int(self.soni_edit.text())
            self.lbl_sum.setText(f" {self.nom}\n {self.soni_edit.text()} donasi = {self.suma} UZS\n\n  Manzilni kiriting\n  To'lovni amalga oshiring")
            self.lbl_sum.show()
            self.btn_sum.hide()
            self.soni_edit.hide()
            self.soni_edit.clear()
            self.name_edit.show()
            self.price_edit.show()
            self.sale_edit.show()
            self.tola_edit.show()
            self.btn_submit.show()
            self.btn_back.show()
        else:
            self.soni_edit.clear()    
            QMessageBox.critical(self,"Xato","Raqam kiriting!!!")

