import eel
import sqlite3


eel.init('web')

def GettingDetailInfoFromDB():
    conn = sqlite3.connect('Demo.db')
    c = conn.cursor()
    cursor = c.execute("SELECT ID,NAME,EMAIL,TELEPHONE, PHONE, ADRESS, ADRESSEXP, HOMEFACILITYTYPE, WORKPLACEFACILITY, STOREFACILITY FROM send WHERE ID=1231321")
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
        eel.info(name,ID,email,telephone, phone, addres, adresExp, Home, workPlace, storage)
    print("Hello")


GettingDetailInfoFromDB()

eel.start('PersonalityInfo.html')