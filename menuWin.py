from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from zakaz import Addmanzil
from query import Kfc_data



class KFCUp(QWidget):
    def __init__(self,reg):
        super().__init__()
        self.registr = reg
        self.resize(1700,900)
        self.setStyleSheet("background:#fff;font-size:20px")

        self.manzilwin = Addmanzil(self)
        self.nom_narx = Kfc_data()

        self.v_main_lay = QVBoxLayout()
        self.v_left_btn_lay = QVBoxLayout()
        self.h_up_btn_lay = QHBoxLayout()
        self.h_down_btn_lay = QHBoxLayout()
        self.list = QScrollArea()
        self.g_lyt = QGridLayout()
        
        self.create_btn()
        self.scroll_btn()     
        self.Upp_menu_btns()
        self.Left_menu_btns()
    def Upp_menu_btns(self):
        
        self.up_menu_btn = QPushButton("KFC")
        self.up_menu_btn.setStyleSheet("background:red;color:white;font-size:60px")
        self.up_menu_btn.setFixedSize(180,150)
        self.menyu_btn = QPushButton("Menu")
        self.menyu_btn.setStyleSheet("background:red;color:white")
        self.menyu_btn.setFixedSize(200,50)
        self.restoran_btn = QPushButton("Restoran")
        self.restoran_btn.setStyleSheet("background:red;color:white")
        self.restoran_btn.setFixedSize(200,50)
        self.halol_btn = QPushButton("Halol")
        self.halol_btn.setStyleSheet("background:green;color:white")
        self.halol_btn.setFixedSize(200,50)
        self.buyurtma_btn = QPushButton("Hozir buyurtma berish")
        self.buyurtma_btn.setStyleSheet("background:red;color:white")
        self.buyurtma_btn.setFixedSize(200,50)
        self.accaunt_btn = QPushButton("Accaunt",clicked=self.accaunt)
        self.accaunt_btn.setStyleSheet("background:lightgray")
        self.accaunt_btn.setFixedSize(80,50)


        self.up_amout_lbl = QLabel("")
        self.up_amout_lbl.setStyleSheet("color:blue")
        self.up_search_edit = QLineEdit()
        self.up_search_edit.setPlaceholderText("search...")
        self.up_contact_center_lbl = QLabel("       Call markaz\n       +998912310880        ")

                
        self.h_up_btn_lay.addWidget(self.up_menu_btn)
        self.h_up_btn_lay.addWidget(self.up_amout_lbl)
        self.h_up_btn_lay.addStretch()
        self.h_up_btn_lay.addWidget(self.menyu_btn)
        self.h_up_btn_lay.addWidget(self.restoran_btn)
        self.h_up_btn_lay.addWidget(self.halol_btn)
        self.h_up_btn_lay.addWidget(self.buyurtma_btn)
        self.h_up_btn_lay.addWidget(self.up_contact_center_lbl)
        self.h_up_btn_lay.addWidget(self.accaunt_btn)
        
        self.v_main_lay.addLayout(self.h_up_btn_lay)
        self.setLayout(self.v_main_lay)    
        
    def Left_menu_btns(self):
        
        self.left_menu_btn = QPushButton("Tavsiya etiladi")
        self.left_menu_btn.setFixedSize(200,50)
        self.left_menu_btn.setStyleSheet("background:yellow")
        self.left_menu_btn.setIconSize(self.left_menu_btn.size())

        self.left_payment_btn = QPushButton("Burgerlar")
        self.left_payment_btn.setFixedSize(200,50)
        self.left_payment_btn.setStyleSheet("background:yellow")
        self.left_payment_btn.setIconSize(self.left_payment_btn.size())

        self.left_transfers_btn = QPushButton("Tvisterlar")
        self.left_transfers_btn.setFixedSize(200,50)
        self.left_transfers_btn.setStyleSheet("background:yellow")
        self.left_transfers_btn.setIconSize(self.left_transfers_btn.size())

        self.left_cards_btn = QPushButton("Basketlar")
        self.left_cards_btn.setFixedSize(200,50)
        self.left_cards_btn.setStyleSheet("background:yellow")
        self.left_cards_btn.setIconSize(self.left_cards_btn.size())
        
        self.left_reports_btn = QPushButton("Suvli tovuq")
        self.left_reports_btn.setFixedSize(200,50)
        self.left_reports_btn.setStyleSheet("background:yellow")
        self.left_reports_btn.setIconSize(self.left_reports_btn.size())

        self.left_main_services_btn = QPushButton("Kartoshka va sneklar")
        self.left_main_services_btn.setFixedSize(200,50)
        self.left_main_services_btn.setStyleSheet("background:yellow")
        self.left_main_services_btn.setIconSize(self.left_main_services_btn.size())


        self.left_auto_payments_btn = QPushButton("Qaylalar va doplar")
        self.left_auto_payments_btn.setFixedSize(200,50)
        self.left_auto_payments_btn.setStyleSheet("background:yellow")
        self.left_auto_payments_btn.setIconSize(self.left_auto_payments_btn.size())

        self.left_settings_btn = QPushButton("Sovup ichimliklar")
        self.left_settings_btn.setFixedSize(200,50)
        self.left_settings_btn.setStyleSheet("background:yellow")
        self.left_settings_btn.setIconSize(self.left_settings_btn.size())

        self.left_issiq_btn = QPushButton("Issiq ichimliklar")
        self.left_issiq_btn.setFixedSize(200,50)
        self.left_issiq_btn.setStyleSheet("background:yellow")
        self.left_issiq_btn.setIconSize(self.left_issiq_btn.size())
        
        self.v_left_btn_lay.addWidget(self.left_menu_btn)
        self.v_left_btn_lay.addWidget(self.left_payment_btn)
        self.v_left_btn_lay.addWidget(self.left_transfers_btn)
        self.v_left_btn_lay.addWidget(self.left_cards_btn)
        self.v_left_btn_lay.addWidget(self.left_reports_btn)
        self.v_left_btn_lay.addWidget(self.left_main_services_btn)
        self.v_left_btn_lay.addWidget(self.left_auto_payments_btn)
        self.v_left_btn_lay.addWidget(self.left_settings_btn)
        self.v_left_btn_lay.addWidget(self.left_issiq_btn)
        
        self.h_down_btn_lay.addLayout(self.v_left_btn_lay)
        self.h_down_btn_lay.addWidget(self.list)
          
        self.v_main_lay.addLayout(self.v_left_btn_lay)
        self.v_main_lay.addLayout(self.h_down_btn_lay)
        self.setLayout(self.v_main_lay)

   

    def create_btn(self):
        self.lts1 = []
        self.taom_btn = self.nom_narx.select_btn()
        for i in self.taom_btn:
            self.nom = i[0].upper()
            self.narx = i[1]
            self.btn = QPushButton(f"{self.nom}\n{self.narx} UZS")
            self.btn.clicked.connect(self.btn_clicked)
            self.btn.setFixedSize(500,300)
            self.btn.setStyleSheet("background:red;color:white;font-size:40px")
            self.lts1.append(self.btn)
        
    def scroll_btn(self):
        self.clear_scroll()
        for i,v in enumerate(self.lts1):
            qator = i // 2
            ustun = i % 2
            self.g_lyt.addWidget(v,qator,ustun)
        oyna = QWidget()
        oyna.setLayout(self.g_lyt)
        self.list.setWidgetResizable(True)
        self.list.setWidget(oyna)
        

    def clear_scroll(self):
        widget = self.list.takeWidget()
        if widget is not None:
            widget.deleteLater()

    def btn_clicked(self):
        self.hide()
        c_btn = self.sender()
        self.txt = c_btn.text()
        temp = self.txt.split("\n")
        temp2 = temp[1].split(" ")
        self.manzilwin.xissob(temp[0].upper(),temp2[0])
        self.manzilwin.show()


    



       
        
    def z1(self):

        self.manzilwin.show()
        self.hide()

    def z2(self):
        self.manzilwin.show()
        self.hide()

    def z3(self):
        self.manzilwin.show()
        self.hide()

    def z4(self):
        self.manzilwin.show()
        self.hide()

    def accaunt(self):
        self.registr.show()
        self.hide()

    
 
 
        
    def Eye_btn(self):
        pass
    
    def Notification(self):
        pass
    
 
        
        
        
        
         
        

       