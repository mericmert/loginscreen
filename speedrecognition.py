import sqlite3
import time
import os

con = sqlite3.connect("Kayitislemleri.db")
imlec = con.cursor()

def sleeper(func):
    def wrapper(*args,**kwargs):
        time.sleep(1)
        func(*args , **kwargs)
    return wrapper

@sleeper
def createTable():
    imlec.execute("CREATE TABLE IF NOT EXISTS kayitlar (Isim TEXT, Sifre Text)")
    con.commit()
@sleeper
def kayitekle(kullanıcı_adi,sifre):
    imlec.execute("INSERT INTO kayitlar VALUES (?,?)",(kullanıcı_adi,sifre))
    con.commit()
    print("Başarıyla Kayıt oldunuz!")
@sleeper
def login(idd,passs):
    imlec.execute("Select * from kayitlar where Isim = ? and Sifre = ?",(idd,passs))
    data =imlec.fetchall()

    if len(data) < 1:
        print("Hatalı giriş yaptınız!")
    else:
        print("Başarıyla giriş yaptınız")

createTable()
print("""
***************************
KAYIT EKRANINA HOS GELDINIZ!
KAYIT OLMAK İCİN 1 E BASINIZ /
GIRIS YAPMAK ICIN 2 YE BASINIZ /
CIKMAK ICIN 3 E BASINIZ/
""")
while True:
    try:
        islem = int(input("Hangi işlemi yapmak istiyorsunuz:"))
    except:
        print("Hatalı işlem kodu.")
        continue
    if islem == 3:
        break
    elif islem ==1:
        kullanıcı_adi = input("Kullanıcı adı:")
        sifre = input("Şifre:")
        kayitekle(kullanıcı_adi, sifre)

    elif islem == 2:
        idd = input("Kullanici adi:")
        passs = input("Şifre:")
        login(idd, passs)
        break



con.close()

