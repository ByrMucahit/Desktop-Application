
import eel
import json
import sqlite3
from sqlite3 import Error
# Write @eel.expose before a python

@eel.expose
def hellopython(text):
    # Create DataBase And Connection
    conn = sqlite3.connect("trials.db")
    c = conn.cursor()

    create_table_general_information = """ CREATE TABLE IF NOT EXISTS general_Information (
                                                    User_Id  integer PRIMARY KEY,
                                                    DATE text,
                                                    User_Name text,
                                                    User_Telephone text,
                                                    User_Phone text,
                                                    User_Address text,
                                                    User_Email text,
                                                    User_Adress_Explanation text,
                                                    Home_Facility_Type text,
                                                    Work_Facility_Type text,
                                                    Store_Facility_Type text,
                                                    Panel_Type text,
                                                    Connection_Type text,
                                                    Seller text,
                                                    Phone_Line text,
                                                    gprs text,
                                                    Network_Line text,
                                                    Montage_Responsibilities text,
                                                    Count_Of_Users integer,
                                                    Count_Person_Who_Will_Called integer,
                                                    Count_Of_Region integer
    ); """

    create_table_user_area = """ CREATE TABLE IF NOT EXISTS User_Info_Area (
                                                                    User_Reference_id_from_User_Section integer, 
                                                                    User_Name text, 
                                                                    User_Email text, 
                                                                    User_Password text, 
                                                                    FOREIGN KEY(User_Reference_id_from_User_Section) REFERENCES general_Information(User_Id));"""
    
    create_table_calling_area = """ CREATE TABLE IF NOT EXISTS User_Who_Will_Called_Stage (
                                                                    User_Reference_id_from_Calling_Section integer, 
                                                                    Name_Of_Person_Who_Will_Called text, 
                                                                    Password_Of_Person_Who_Will_Called text, 
                                                                    Telephone_Of_Person_Who_Will_Called text, 
                                                                    gsm1_Of_Person_Who_Will_Called text, 
                                                                    gsm2_Of_Person_Who_Will_Called text, 
                                                                    gsm3_Of_Person_Who_Will_Called text, 
                                                                    FOREIGN KEY(User_Reference_id_from_Calling_Section) REFERENCES general_Information(User_Id)); """

    create_table_region_area = """ CREATE TABLE IF NOT EXISTS region_info_area ( 
                                                                                user_id_from_region_area integer, 
                                                                                Region text, 
                                                                                FOREIGN KEY(user_id_from_region_area) REFERENCES general_Information(User_Id)) """

    try:
        # Getting Value From Input Throughout Variables
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
        
    except(Error) :
        print("This is Error Message --> {}".format(Error))   

    try:
        c.execute(create_table_general_information)
        c.execute("INSERT INTO general_Information (User_Id, DATE, User_Name, User_Telephone, User_Phone, User_Address, User_Email, User_Adress_Explanation, Home_Facility_Type, Work_Facility_Type, Store_Facility_Type, Panel_Type, Connection_Type, Seller, Phone_Line,  gprs, Network_Line, Montage_Responsibilities) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(Number_Of_Account, Date, Name_Of_Account, Account_Telephone, Account_Phone, Account_Adress, Account_Email, Address_Explanation, Type_Of_facility_Home, Type_Of_facility_WorkPlace, Type_Of_Facility_Store, Type_Of_Panel, Type_Of_Connection,Seling_Personel, Line_Of_Phone, GPRS, Line_Of_Net, assembly_Personel))
        users_Informations = c.execute("SELECT User_Id, DATE, User_Name, User_Telephone, User_Phone, User_Address, User_Email, User_Adress_Explanation, Home_Facility_Type, Work_Facility_Type, Store_Facility_Type, Panel_Type, Connection_Type,Seller, Phone_Line, gprs, Network_Line, Montage_Responsibilities FROM general_Information")
        for raw in users_Informations:
            print("ID FROM DB--> {}".format(raw[0]))
            print("DATE --> {}".format(raw[1]))
            print("Name Of Account --> {}".format(raw[2]))
            print("Telephone Of Account --> {}".format(raw[3]))
            print("Phone Of Account --> {}".format(raw[4]))
            print("Address Of Account --> {}".format(raw[5]))
            print("Email Of Account --> {}".format(raw[6]))
            print("Adress Explanation --> {}".format(raw[7]))
            print("Home Facility --> {}".format(raw[8]))
            print("Work Facility --> {}".format(raw[9]))
            print("Store Facility --> {}".format(raw[10]))
            print("Panel Type --> {}".format(raw[11]))
            print("Connection Type --> {}".format(raw[12]))
            print("Seller --> {}".format(raw[13]))
            print("Phone Line --> {}".format(raw[14]))
            print("Gprs Line --> {}".format(raw[15]))
            print("Network Line --> {}".format(raw[16]))
            print("Montage Response --> {}".format(raw[17]))
        conn.commit()
        print("Hello")
        
    except(Error):
        print("This is error mesafe from General Information -> {}".format(Error))
        eel.ErrorMessage(Error)
   
    try:
        c = conn.cursor()
        c.execute(create_table_user_area)

        for i in range(1,userCount+1):
            print("{} . name --> {}".format(i,user[str(i)+"name"]))
            name = user[str(i)+"name"]
            print("{} . email --> {}".format(i,user[str(i)+"email"]))
            email = user[str(i)+"email"]
            print("{} . password --> {}".format(i,user[str(i)+"password"]))
            password = user[str(i)+"password"]
            c.execute("INSERT INTO User_Info_Area (User_Reference_id_from_User_Section, User_Name, User_Email, User_Password) VALUES (?, ?, ?, ?)", (Number_Of_Account, name, email, password))

        user_info_cursor = c.execute("SELECT User_Reference_id_from_User_Section, User_Name, User_Email, User_Password FROM User_Info_Area")
        for i,user in enumerate(user_info_cursor):
            print("{}. id from user info area --> {}".format(i,user[0]))
            print("{}. User_Name from user info area --> {}".format(i,user[1]))
            print("{}. User_Email from user info area --> {}".format(i,user[2]))
            print("{}. User_Password from user info area --> {}".format(i,user[3]))
        conn.commit()
        
    except(Error):
        print("This is Error Message from User Info DB --> {}".format(Error))
        eel.ErrorMessage(Error)

    
    try:
        c = conn.cursor()
        c.execute(create_table_calling_area)
        for j in range(1,countWhowillCalling+1):
            print("{} . isim --> {}".format(j,personeWhoWillCalled[str(j)+"isim"]))
            Name_Of_Person_Who_Will_Called = personeWhoWillCalled[str(j)+"isim"]

            print("{} . sifre --> {}".format(j,personeWhoWillCalled[str(j)+"sifre"]))
            Password_Of_Person_Who_Will_Called = personeWhoWillCalled[str(j)+"sifre"]

            print("{} . telefon --> {}".format(j,personeWhoWillCalled[str(j)+"telefon"]))
            Telephone_Of_Person_Who_Will_Called = personeWhoWillCalled[str(j)+"telefon"]

            print("{} . GSM1 --> {}".format(j,personeWhoWillCalled[str(j)+"GSM1"]))
            gsm1_Of_Person_Who_Will_Called = personeWhoWillCalled[str(j)+"GSM1"]

            print("{} . GSM2 --> {}".format(j,personeWhoWillCalled[str(j)+"GSM2"]))
            gsm2_Of_Person_Who_Will_Called = personeWhoWillCalled[str(j)+"GSM2"]

            print("{} . GSM3 --> {}".format(j,personeWhoWillCalled[str(j)+"GSM3"]))
            gsm3_Of_Person_Who_Will_Called = personeWhoWillCalled[str(j)+"GSM3"]
            
            c.execute("INSERT INTO User_Who_Will_Called_Stage (User_Reference_id_from_Calling_Section,Name_Of_Person_Who_Will_Called, Password_Of_Person_Who_Will_Called, Telephone_Of_Person_Who_Will_Called, gsm1_Of_Person_Who_Will_Called, gsm2_Of_Person_Who_Will_Called, gsm3_Of_Person_Who_Will_Called) VALUES(?, ?, ?, ?, ?, ?, ?)",(Number_Of_Account, Name_Of_Person_Who_Will_Called, Password_Of_Person_Who_Will_Called, Telephone_Of_Person_Who_Will_Called, gsm1_Of_Person_Who_Will_Called, gsm2_Of_Person_Who_Will_Called, gsm3_Of_Person_Who_Will_Called))
            print("Person Who will called Info has been added.")
            
        calling_person_cursor = c.execute("SELECT User_Reference_id_from_Calling_Section,Name_Of_Person_Who_Will_Called, Password_Of_Person_Who_Will_Called, Telephone_Of_Person_Who_Will_Called, gsm1_Of_Person_Who_Will_Called, gsm2_Of_Person_Who_Will_Called, gsm3_Of_Person_Who_Will_Called FROM User_Who_Will_Called_Stage")
        for call in calling_person_cursor:
            print(" ID from call db---> {}".format(call[0]))
            print(" Name from call db---> {}".format(call[1]))
            print(" Password from call db --> {}".format(call[2]))
        conn.commit()
    except(Error):
        print("this is an error message from call db--> {}".format(Error))
        eel.ErrorMessage(Error)

    try:
        c = conn.cursor()
        c.execute(create_table_region_area)
        for t in range(1, regionCount+1):
            print("{} . Bolge --> {}".format(t,Region[str(t)+"Region"]))
            region = Region[str(t)+"Region"]
            c.execute('INSERT INTO region_info_area (user_id_from_region_area, Region) VALUES (?, ?)', (Number_Of_Account, region))
            
        
        region_cursor = c.execute("SELECT user_id_from_region_area, Region FROM region_info_area")
        for  counter,reg in enumerate(region_cursor):
            print("{}. Region Into Database --> {} ".format(counter,reg[1]))
            print("{}. ID Into Database --> {} ".format(counter,reg[0]))
        conn.commit()
    except(Error):
        print("this is an error message from region db--> {}".format(Error))
        eel.ErrorMessage(Error)

        

    c.close()
    conn.close()
  
eel.init('web')
eel.start('main.html')