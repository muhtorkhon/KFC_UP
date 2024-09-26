import mysql.connector
class Kfc_data:
    def __init__(self):
        self.connector()
        self.createDB()
        self.createTB()


    def connector(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "your password enter"
        )
        self.cursor = self.mydb.cursor()

    def createDB(self):
        self.cursor.execute("create database if not exists KFC_com")
        self.cursor.execute("use KFC_com")

    def createTB(self):
        self.cursor.execute("""create table if not exists kfc_shop (id int auto_increment primary key,
                            name varchar(100),
                            price real,
                            sale int)""")

    def insertData(self,bookdata):
        cur = ("""insert into kfc_shop(name,
                            price,
                            sale) values(%s,%s,%s)""")
        self.cursor.execute(cur,bookdata)
        self.mydb.commit()

    def select_all(self):
        self.cursor.execute("select * from kfc_shop")
        self.temp = self.cursor.fetchall()
        return self.temp
    def select_price(self,price):
        self.cursor.execute(f"select price from kfc_shop where price = {price}")
        self.temp = self.cursor.fetchall()
        return self.temp
    def select_btn(self):
        self.cursor.execute(f'select name, price from kfc_shop')
        self.temp = self.cursor.fetchall()
        return self.temp

    def clousss(self):
        self.mydb.close()




class Manzil:
    def __init__(self):
        self.connector()
        self.createDB()
        self.createTB()


    def connector(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "your password enter"
        )
        self.cursor = self.mydb.cursor()

    def createDB(self):
        self.cursor.execute("create database if not exists manzillar")
        self.cursor.execute("use manzillar")

    def createTB(self):
        self.cursor.execute("""create table if not exists manzil (id int auto_increment primary key,
                            shaxar varchar(100),
                            kocha varchar(100),
                            uy varchar(100))""")

    def insertData(self,addadres):
        cur = ("""insert into manzil(shaxar,
                            kocha,
                            uy) values(%s,%s,%s)""")
        self.cursor.execute(cur,addadres)
        self.mydb.commit()

    def select_manzil(self):
        self.cursor.execute("select * from manzil)")
        self.temp = self.cursor.fetchall()
        return self.temp

    def clousss(self):
        self.mydb.close()

