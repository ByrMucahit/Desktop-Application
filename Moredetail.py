import eel
import sqlite3


eel.init('web')
conn = sqlite3.connect('trials.db')
c = conn.cursor()
def GettingDetailInfoFromDB():
    cursor = c.execute("SELECT ID,NAME,EMAIL,TELEPHONE, PHONE, ADRESS, ADRESSEXP, HOMEFACILITYTYPE, WORKPLACEFACILITY, STOREFACILITY, PANELTYPE, CONNECTIONTYPE, SELLER, PHONELINE, GPRS, NETLINE, MONTAJ_SORUMLUSU, KullaniciSayisi, AranacakKisiSayisi, BolgeSayisi FROM send WHERE ID=18121069")
    for raw in cursor:
        ID = raw[0]
        name = raw[1]
        email = raw[2]
        telephone = raw[3]
        phone = raw[4]
        addres = raw[5]
        adresExp = raw[6]
        Home = raw[7]
        workPlace = raw[8]
        storage = raw[9]
        paneltype = raw[10]
        conType = raw[11]
        Seller = raw[12]
        phoneL = raw[13]
        gprs = raw[14]
        networkLine = raw[15]
        montaj = raw[16]
        userCount = raw[17]
        personWhoWillCall = raw[18]
        regionCnt = raw[19]
    eel.info(name,ID,email,telephone, phone, addres, adresExp, Home, workPlace, storage, paneltype, conType, Seller, phoneL, gprs, networkLine, montaj, userCount, personWhoWillCall, regionCnt)
    
    user_cursor = c.execute("SELECT User_Name From Users") 
    
    for i,raw in enumerate(user_cursor):
        print("{} . Name From DB --> {} ".format(i, raw[0]))
        Uname = raw[0]
       
        eel.S(Uname)
        
        
    

    
    

    

GettingDetailInfoFromDB()


c.close()
conn.close()
eel.start('PersonalityInfo.html')