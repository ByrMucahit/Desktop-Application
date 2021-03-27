import eel
import sqlite3


eel.init('web')

def GettingDetailInfoFromDB():
    con = sqlite3.connect("trials.db")
    con.text_factory = sqlite3.OptimizedUnicode
    c = con.cursor()
    
    
    
 



    
    cursor = c.execute("SELECT User_Id, User_Name, DATE,  User_Email,User_Telephone, User_Phone, User_Address, User_Adress_Explanation, Home_Facility_Type, Work_Facility_Type, Store_Facility_Type, Panel_Type, Connection_Type, Seller, Phone_Line, gprs, Network_Line, Montage_Responsibilities, Count_Of_Users, Count_Person_Who_Will_Called, Count_Of_Region FROM general_Information")
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
    
    
    
    
    


    
       
def Show_Tables_Inside_Database():
    con = sqlite3.connect("trials.db")
    cursor = con.cursor()
    print(cursor.fetchall())

    cursor.close()
    con.close()
    

        
        
    

    
    

    

GettingDetailInfoFromDB()
Show_Tables_Inside_Database()



eel.start('PersonalityInfo.html')