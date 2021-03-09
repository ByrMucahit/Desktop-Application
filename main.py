
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
    print(Regions)
    
    con = sqlite3.connect('mydatabase.db')
    cursorOb = con.cursor()

    try:
        
        print("Connection is established: Database is created in memory")
    except Error:
        print(Error)
    



   

eel.init('web')
eel.start('main.html')