import eel
import sqlite3

eel.init('web')

@eel.expose
def GettingInfoFromDB():
    conn = sqlite3.connect('trials.db')
    c = conn.cursor()
    cursor = c.execute('SELECT User_Id, DATE, User_Name, User_Telephone, User_Phone, User_Address, User_Email, User_Adress_Explanation, Home_Facility_Type, Work_Facility_Type, Store_Facility_Type, Panel_Type, Connection_Type,Seller, Phone_Line, gprs, Network_Line, Montage_Responsibilities FROM general_Information')

    for raw in cursor:
        print("ID --> ", raw[0])
        ID = raw[0]

        print("DATE --> ",raw[1])
        date = raw[1]

        print("NAME -->",raw[2])
        name = raw[2]

        print("Telephone --> ",raw[3])
        telephone = raw[3]

        print("PHONE --> ",raw[4])
        Phone = raw[4]

        print("Address --> ",raw[5])
        Adress = raw[5]

        print("Email --> ",raw[6])
        email = raw[6],

        print("Address Aciklamasi -->",raw[7])
        adres_Explanation = raw[7]

        print("Ev Tesis Tipi -->", raw[8])
        homeFacility = raw[8]

        print("İs Yeri Tesis Tipi -->", raw[9])
        workPlace = raw[9]

        print("Depo Tesis Tipi")
        store = raw[10]

        print("Panel Tipi --> ",raw[11])
        panel = raw[11]

        print("Baglanti Tipi -->", raw[12])
        connectionType = raw[12]

        print("Satis Elemani -->", raw[13])
        seller = raw[13]

        print("Telefon Hatti -->", raw[14])
        PhoneLine = raw[14]

        print("GPRS --> ", raw[15])
        GPRS = raw[15]

        print("Net hatti --> ", raw[16])
        NetLine = raw[16]

        print("Montaj Sorumlusu -->", raw[17])
        montaj = raw[17]

        eel.hello_js(ID, date, name, telephone, Phone, Adress, email, adres_Explanation, homeFacility, workPlace, store, panel, connectionType, seller, PhoneLine, GPRS, NetLine, montaj)
        
    c.close()
    conn.close()

@eel.expose
def sended(value):
    print("this is other lib ",value)
    


GettingInfoFromDB()


eel.start('Info.html')