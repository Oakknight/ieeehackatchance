# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 20:11:31 2019

@author: Oguz
"""

#Butun fonksiyonlar detaylica 'documentation.txt' dosyasında aciklanmistir

def idBulma(ilacIsim): #ilacin isminden yola cikarak ilacin veritabanindaki id'sine erismek icin kullanilir
    ilacID = ilacVeriTabani.execute("SELECT id FROM ilaclar WHERE isim=?", (ilacIsim,)).fetchall()
    return(ilacID[0][0])
    
def isimBulma(ilacID): #ilacin veritabanindaki id'sinden yola cikarak ilacin ismine erismek icin kullanilir 
    ilacIsim = ilacVeriTabani.execute("SELECT isim FROM ilaclar WHERE id=?", (ilacID,)).fetchall()
    return(ilacIsim[0][0])
    
def TCdenID(TC): #hastanin Turkiye Cumhuriyeti kimlik numarasından veritabanindaki id'sine eriskek icin kullanilir
    hastaID = hastaVeriTabani.execute("SELECT id FROM hastalar WHERE TC=?", (TC,)).fetchall()
    return(hastaID[0][0])

def kullanma(ilacID): #id'si ilacID olan ilacla beraber kullanilmamasi gereken ilaclarin id'lerini almak icin kullanilir
    ilac = ilacVeriTabani.execute("SELECT kullanma FROM ilaclar").fetchall()
    ilacStr = "".join(ilac[ilacID-1][0])
    ilacStr = ilacStr.split(",")
    return(ilacStr)

def ilacBilgi(ilacID): #veritabanidaki ilacin bilgilerini almak için kullanılır
    isim = ilacVeriTabani.execute("SELECT isim FROM ilaclar").fetchall()
    tag = ilacVeriTabani.execute("SELECT tag FROM ilaclar").fetchall()
    antibiyotik = ilacVeriTabani.execute("SELECT antibiyotik FROM ilaclar").fetchall()
    agri = ilacVeriTabani.execute("SELECT agri FROM ilaclar").fetchall()
    antidep = ilacVeriTabani.execute("SELECT antidep FROM ilaclar").fetchall()
    dogum = ilacVeriTabani.execute("SELECT dogum FROM ilaclar").fetchall()
    inceltici = ilacVeriTabani.execute("SELECT inceltici FROM ilaclar").fetchall()
    NSAID = ilacVeriTabani.execute("SELECT NSAID FROM ilaclar").fetchall()
    bobrek = ilacVeriTabani.execute("SELECT bobrek FROM ilaclar").fetchall()
    hamile = ilacVeriTabani.execute("SELECT hamile FROM ilaclar").fetchall()
    kalp = ilacVeriTabani.execute("SELECT kalp FROM ilaclar").fetchall()
    diyabet = ilacVeriTabani.execute("SELECT diyabet FROM ilaclar").fetchall()
    hemo = ilacVeriTabani.execute("SELECT hemo FROM ilaclar").fetchall()
    aciklama = ilacVeriTabani.execute("SELECT aciklama FROM ilaclar").fetchall()
    return(isim[ilacID-1][0], tag[ilacID-1][0], kullanma(ilacID), antibiyotik[ilacID-1][0], agri[ilacID-1][0], antidep[ilacID-1][0], dogum[ilacID-1][0], inceltici[ilacID-1][0],
           NSAID[ilacID-1][0], bobrek[ilacID-1][0], hamile[ilacID-1][0], kalp[ilacID-1][0], diyabet[ilacID-1][0], hemo[ilacID-1][0], aciklama[ilacID-1][0])
    
def ilacIsimleri(): #veritabanindaki tum ilaclarin isimlerini geri verir
    isimDatabase = ilacVeriTabani.execute("SELECT isim FROM ilaclar").fetchall()
    isimler = []
    for i in range(0, len(isimDatabase)):
        isimler.append(isimDatabase[i][0])
    return(isimler)
    
def kullanilan(hastaID): #hastanın kullandıgı ilaclarin id'lerini geri verir 
    hasta = hastaVeriTabani.execute("SELECT kullanilan FROM hastalar").fetchall()
    hastaStr = "".join(hasta[hastaID-1][0])
    hastaStr = hastaStr.split(",")
    return(hastaStr)
    
def hastaBilgi(hastaID): #hastanin veritabanindaki bilgilerini almak icin kullanilir
    isim = hastaVeriTabani.execute("SELECT isim FROM hastalar").fetchall()
    TC = hastaVeriTabani.execute("SELECT TC FROM hastalar").fetchall()
    bobrek = hastaVeriTabani.execute("SELECT bobrek FROM hastalar").fetchall()
    hamile = hastaVeriTabani.execute("SELECT hamile FROM hastalar").fetchall()
    kalp = hastaVeriTabani.execute("SELECT kalp FROM hastalar").fetchall()
    diyabet = hastaVeriTabani.execute("SELECT diyabet FROM hastalar").fetchall()
    hemo = hastaVeriTabani.execute("SELECT hemo FROM hastalar").fetchall()
    return(isim[hastaID-1][0], TC[hastaID-1][0], kullanilan(hastaID), bobrek[hastaID-1][0], hamile[hastaID-1][0], kalp[hastaID-1][0], diyabet[hastaID-1][0], hemo[hastaID-1][0])
    

def ilacKontrol(TC, ilacIsim): #hastanin belirli bir ilaci kullanmasinda bir sakinca olup olmadigini kontrol eder
    sinirlama = []
    hastaID = TCdenID(TC)
    ilacID = idBulma(ilacIsim)
    for i in range(0, len(kullanilan(hastaID))):
        for j in range(0, len(kullanma(ilacID))):
            if(kullanilan(hastaID)[i] == kullanma(ilacID)[j]):
                sinirlama.append(isimBulma(kullanilan(hastaID)[i]) + "ve" + ilacIsim + " birlikte kullanılamaz") 
    
    for l in range(0, len(kullanilan(hastaID))):
        ilacTipi = ilacBilgi(int(kullanilan(hastaID)[l]))[1] + 2
        if(ilacTipi == 3):
            sinirlama.append(ilacIsim + ", antibiyotiklerle kullanılamaz")
        elif(ilacTipi == 4):
            sinirlama.append(ilacIsim + ", ağrı kesicilerle kullanılamaz")
        elif(ilacTipi == 5):
            sinirlama.append(ilacIsim + ", antidepresanlarla kullanılamaz")
        elif(ilacTipi == 6):
            sinirlama.append(ilacIsim + ", doğum kontrol haplarıyla kullanılamaz")
        elif(ilacTipi == 7):
            sinirlama.append(ilacIsim + ", kan incelticilerle kullanılamaz")
        elif(ilacTipi == 8):
            sinirlama.append(ilacIsim + ", anti-inflamatörlerle kullanılamaz")
            
    for m in range(0, 5):
        if(m == 1 and hastaBilgi(hastaID)[m + 3] == 1):
            sinirlama.append("Gebeliğin " + str(ilacBilgi(ilacID)[m + 9]) + ". ayına kadar kullanılabilir")
        else:
            if(hastaBilgi(hastaID)[m + 3] == ilacBilgi(ilacID)[m + 9]):
                if(m == 0):
                    sinirlama.append("Böbrek yetmezliği durumlarında" + ilacBilgi(ilacID)[0] + "kullanılamaz")
                elif(m == 2):
                    sinirlama.append("Kalp damar rahatsızlıkları durumlarında" + ilacBilgi(ilacID)[0] + "kullanılamaz")
                elif(m == 3):
                    sinirlama.append("Diyabet durumlarında" + ilacBilgi(ilacID)[0] + "kullanılamaz")
                elif(m == 4):
                    sinirlama.append("Hemofili durumlarında" + ilacBilgi(ilacID)[0] + "kullanılamaz")
        
        
    return(sinirlama)
        

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import sqlite3

ilacBaglanti = sqlite3.connect("ilaclar.db")
hastaBaglanti = sqlite3.connect("hastalar.db")

if(ilacBaglanti):
    print('Ilaclar baglantisi basarili!')
else:
    print('Ilaclar baglantisi basarisiz!')
    
if(hastaBaglanti):
    print('Hastalar baglantisi basarili!')
else:
    print('Hastalar baglantisi basarisiz!')
    
    
    
ilacVeriTabani = ilacBaglanti.cursor()
hastaVeriTabani = hastaBaglanti.cursor()

ilacKontrol(30909671126, " Ibuprofen(Oral) ")

ilacBaglanti.commit()
ilacBaglanti.close()

hastaBaglanti.commit()
hastaBaglanti.close()

