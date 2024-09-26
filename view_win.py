from PyQt5.QtWidgets import *
from query import *

class View(QWidget):
    def __init__(self,win_main):
        super().__init__()
        self.win_show = win_main

        self.data = Kfc_data()
        self.all_manzil = Manzil()

        self.setFixedSize(520,620)
        self.setStyleSheet("font-size:20px")

        self.h_btn_lyt = QHBoxLayout()
        self.v_main_lyt = QVBoxLayout()

        self.lts = QListWidget()

        self.janr_btn = QPushButton("Barcha taomlar",clicked = self.savol1)
        self.janr_btn.setFixedSize(150,60)
        self.janr_btn.setStyleSheet("background:red;color:white")

        self.adr_btn = QPushButton("Barcha manzillar",clicked = self.adres)
        self.adr_btn.setFixedSize(150,60)
        self.adr_btn.setStyleSheet("background:red;color:white")

        self.back_btn = QPushButton("Back",clicked = self.back_m)
        self.back_btn.setStyleSheet("background:red;color:white")
        self.back_btn.setFixedSize(150,60)

        self.h_btn_lyt.addWidget(self.janr_btn)
        self.h_btn_lyt.addWidget(self.adr_btn)
        self.h_btn_lyt.addWidget(self.back_btn)

        self.v_main_lyt.addWidget(self.lts)
        self.v_main_lyt.addLayout(self.h_btn_lyt)

        self.setLayout(self.v_main_lyt)

    def savol1(self):

        self.lts.clear()
        try:
            data_1 = self.data.select_all()
            for i in data_1:
                self.lts.addItem(f"""ID: {i[0]}
Nomi: {i[1]}
Narxi: {i[2]}
Soni: {i[3]}""")
        except:
            QMessageBox.critical(self,"xato","Taomlar yo'q!!!")

    def adres(self):
        self.lts.clear()
        try:
            data_1 = self.all_manzil.select_manzil()
            for i in data_1:
                self.lts.addItem(f"""ID: {i[0]}
Shahar: {i[1]}
Ko'cha: {i[2]}
Uy: {i[3]}""")
        except:
            QMessageBox.critical(self,"xato","Manzil yo'q!!!")

    def back_m(self):
        self.hide()
        self.win_show.show()


