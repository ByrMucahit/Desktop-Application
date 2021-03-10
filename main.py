
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
    
    # Create DataBase And Connection
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    conn.execute('''CREATE TABLE IF NOT EXISTS Aybekler
                (ID INT PRIMARY KEY NOT NULL) ''')
    
    try:
        conn.execute("INSERT INTO Aybekler VALUES(1)")
        conn.commit
        print("got it")
        cursor = conn.execute("SELECT ID FROM Aybekler")
        for row in cursor:
            print("id -> ",row[0])  
    except Error:
        print(Error)
    conn.close()

    
eel.init('web')
eel.start('main.html')