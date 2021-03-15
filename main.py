
import eel
import json
import sqlite3
from sqlite3 import Error
# Write @eel.expose before a python

@eel.expose
def hellopython(text):
    Date = text['date']
    Number_Of_Account = text['AboneNo']
    Name_Of_Account = text["AboneAdı"]
    Account_Telephone = text['AboneTelefon']
    Account_Phone = text['AboneCepTelefon']
    Account_Adress = text['AboneAdress']
    Account_Email = text['AboneEmail']
    Address_Explanation = text['AboneAdresAciklamasi']
    Type_Of_facility_Home = text['EvTesisTipi']
    Type_Of_facility_WorkPlace = text['Isyeri']
    Type_Of_Facility_Store = text['Depo']
    Type_Of_Panel = text["PanelTipi"]
    Type_Of_Connection = text["BağlantıTipi"]
    Seling_Personel = text['SatisPersoneli']
    Line_Of_Phone = text['TelefonHatti']
    GPRS = text['GPRS']
    Line_Of_Net = text['InternetHatti']
    assembly_Personel = text['MontajSorumlusu']
    users = text['Kullanıcılar']
    call = text['AranacakKisiler']
    open_close = text['Acik_Kapali']
    weekend_Service = text['HaftasonuHizmet']
    Regions = text['Bolgeler']
    userCount = int(text['KullaniciSayisi'])
    countWhowillCalling= int(text['AranacakKisiSayisi'])
    regionCount = int(text['BolgeSayisi'])
    user = text['Kullanıcılar']
    personeWhoWillCalled = text['AranacakKisiler']
    Region = text['Bolgeler']
    # Create DataBase And Connection
    conn = sqlite3.connect("Demo.db")
    c = conn.cursor()
   
    # QUERY TRANSACTION
    c.execute("CREATE TABLE IF NOT EXISTS SSZE (ID  REAL ,DATE TEXT, NAME TEXT, TELEPHONE TEXT, PHONE TEXT, ADRESS TEXT, EMAIL TEXT, ADRESSEXP TEXT, HOMEFACILITYTYPE TEXT, WORKPLACEFACILITY TEXT, STOREFACILITY TEXT, PANELTYPE TEXT, CONNECTIONTYPE TEXT, SELLER TEXT, PHONELINE TEXT, GPRS TEXT, NETLINE TEXT, MONTAJ_SORUMLUSU TEXT, KullaniciSayisi TEXT, AranacakKisiSayisi TEXT, BolgeSayisi TEXT)")
    c.execute("INSERT INTO SSZE (ID, DATE, NAME, TELEPHONE, PHONE, ADRESS, EMAIL, ADRESSEXP, HOMEFACILITYTYPE, WORKPLACEFACILITY, STOREFACILITY, PANELTYPE, CONNECTIONTYPE, SELLER, PHONELINE, GPRS, NETLINE, MONTAJ_SORUMLUSU,KullaniciSayisi , AranacakKisiSayisi , BolgeSayisi ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(Number_Of_Account, Date, Name_Of_Account, Account_Telephone, Account_Phone, Account_Adress, Account_Email, Address_Explanation, Type_Of_facility_Home, Type_Of_facility_WorkPlace, Type_Of_Facility_Store, Type_Of_Panel, Type_Of_Connection, Seling_Personel, Line_Of_Phone, GPRS, Line_Of_Net, assembly_Personel, userCount, countWhowillCalling, regionCount))
    conn.commit()

    cursor = c.execute("SELECT ID, DATE, NAME, TELEPHONE, PHONE, ADRESS, EMAIL, ADRESSEXP, HOMEFACILITYTYPE, WORKPLACEFACILITY, STOREFACILITY, PANELTYPE, CONNECTIONTYPE, SELLER, PHONELINE, GPRS, NETLINE, MONTAJ_SORUMLUSU, KullaniciSayisi , AranacakKisiSayisi , BolgeSayisi  FROM SSZE")
    for raw in cursor:
        print("ID --> ", raw[0])
        print("DATE -> ", raw[1])
        print("Name -> ", raw[2])
        print("Telephone -> ", raw[3])
        print("Phone -> ", raw[4])
        print("ADRESS ->", raw[5])
        print("Email ->", raw[6])
        print("Adres Aciklamasi  ->", raw[7])
        print("ev  ->", raw[8])
        print("Is Yeri  ->", raw[9])
        print("Depo  ->", raw[10])
        print("Panel Tipi  ->", raw[11])
        print("Bağlantı Tipi ->", raw[12])
        print("Satis Elemani -> ", raw[13])
        print("Telefon Hattı -> ", raw[14])
        print("GPRS -> ", raw[15])
        print("NetHattı -> ", raw[16])
        print("Montaj Sorumlusu -> ", raw[17])
        print("Kullanici Sayisi -> ", raw[18])
        print("Aranacak Kisi Sayisi -> ", raw[19])
        print("Bölge Sayisi -> ", raw[20])
    for i in range(1,userCount+1):
        print("{} . name --> {}".format(i,user[str(i)+"name"]))
        print("{} . email --> {}".format(i,user[str(i)+"email"]))
        print("{} . password --> {}".format(i,user[str(i)+"password"]))
    for j in range(1,countWhowillCalling+1):
        print("{} . isim --> {}".format(j,personeWhoWillCalled[str(j)+"isim"]))
        print("{} . sifre --> {}".format(j,personeWhoWillCalled[str(j)+"sifre"]))
        print("{} . telefon --> {}".format(j,personeWhoWillCalled[str(j)+"telefon"]))
        print("{} . GSM1 --> {}".format(j,personeWhoWillCalled[str(j)+"GSM1"]))
        print("{} . GSM2 --> {}".format(j,personeWhoWillCalled[str(j)+"GSM2"]))
        print("{} . GSM3 --> {}".format(j,personeWhoWillCalled[str(j)+"GSM3"]))
    for t in range(1, regionCount+1):
        print("{} . Bolge --> {}".format(t,Region[str(t)+"Region"]))
        

    c.close()
    conn.close()




    
eel.init('web')
eel.start('main.html')