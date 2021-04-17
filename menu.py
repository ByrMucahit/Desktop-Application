import eel
import sqlite3
from sqlite3 import Error
import io
eel.init('web')


def backup():
    from datetime import date # Getting date

    today = date.today() # Getting today 
    #print("Today's date:", today)
    d1 = today.strftime("%d") # Get only day
    if(d1 == "07" or d1 == "14" or d1 == "21" or d1 == "28"): # if day would be that I want to .
        conn = sqlite3.connect('aybekler1aszDB.db') # Back up
        with io.open('clientes_dump.sql', 'w') as f: # write on file
            for linha in conn.iterdump(): # travel line to line.
                f.write('%s\n' % linha)
        #print('Backup performed successfully.')
        #print('Saved as mydatabase_dump.sql')
        conn.close()


backup()


@eel.expose
def hellopython(text):
    print("It is working")
    try:
        # Create DataBase And Connection
        conn = sqlite3.connect("aybekler1aszDB.db")
        c = conn.cursor()
    except:
        print("Database can not connected.")

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
                                                    open_close text,
                                                    saturday_open_close text,
                                                    sunday_open_close text

    ); """

    create_table_user_area = """ CREATE TABLE IF NOT EXISTS User_Info_Area (
                                                                    User_Reference_id_from_User_Section integer, 
                                                                    User_Name text, 
                                                                    User_Email text, 
                                                                    User_Password text, 
                                                                    Count_Of_Users integer,
                                                                    FOREIGN KEY(User_Reference_id_from_User_Section) REFERENCES general_Information(User_Id));"""

    create_table_calling_area = """ CREATE TABLE IF NOT EXISTS User_Who_Will_Called_Stage (
                                                                    User_Reference_id_from_Calling_Section integer, 
                                                                    Name_Of_Person_Who_Will_Called text, 
                                                                    Password_Of_Person_Who_Will_Called text, 
                                                                    Telephone_Of_Person_Who_Will_Called text, 
                                                                    gsm1_Of_Person_Who_Will_Called text, 
                                                                    gsm2_Of_Person_Who_Will_Called text, 
                                                                    gsm3_Of_Person_Who_Will_Called text, 
                                                                    Count_Person_Who_Will_Called integer,
                                                                    FOREIGN KEY(User_Reference_id_from_Calling_Section) REFERENCES general_Information(User_Id)); """

    create_table_region_area = """ CREATE TABLE IF NOT EXISTS region_info_area ( 
                                                                                user_id_from_region_area integer, 
                                                                                Region text, 
                                                                                Count_Of_Region integer,
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
        countWhowillCalling = int(text['AranacakKisiSayisi'])
        regionCount = int(text['BolgeSayisi'])
        user = text['Kullanıcılar']
        personeWhoWillCalled = text['AranacakKisiler']
        Region = text['Bolgeler']
        open_close = text['Acik_Kapali']
        weekend_close = text['HaftasonuHizmet']

    except(Error):
        print("This is Error Message --> {}".format(Error))

    try:
        print("Cumartesi", weekend_close['Cumatesi'])
        c.execute(create_table_general_information)
        c.execute("INSERT INTO general_Information (User_Id, DATE, User_Name, User_Telephone, User_Phone, User_Address, User_Email, User_Adress_Explanation, Home_Facility_Type, Work_Facility_Type, Store_Facility_Type, Panel_Type, Connection_Type, Seller, Phone_Line,  gprs, Network_Line, Montage_Responsibilities, open_close, saturday_open_close, sunday_open_close) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (Number_Of_Account, Date, Name_Of_Account, Account_Telephone, Account_Phone, Account_Adress, Account_Email, Address_Explanation, Type_Of_facility_Home, Type_Of_facility_WorkPlace, Type_Of_Facility_Store, Type_Of_Panel, Type_Of_Connection, Seling_Personel, Line_Of_Phone, GPRS, Line_Of_Net, assembly_Personel, open_close, weekend_close['Cumatesi'], weekend_close['Pazar']))
        users_Informations = c.execute("SELECT User_Id, DATE, User_Name, User_Telephone, User_Phone, User_Address, User_Email, User_Adress_Explanation, Home_Facility_Type, Work_Facility_Type, Store_Facility_Type, Panel_Type, Connection_Type,Seller, Phone_Line, gprs, Network_Line, Montage_Responsibilities, open_close, saturday_open_close, sunday_open_close FROM general_Information")
        # for raw in users_Informations:
        #print("ID FROM DB--> {}".format(raw[0]))
        #print("DATE --> {}".format(raw[1]))
        #print("Name Of Account --> {}".format(raw[2]))
        #print("Telephone Of Account --> {}".format(raw[3]))
        #print("Phone Of Account --> {}".format(raw[4]))
        #print("Address Of Account --> {}".format(raw[5]))
        #print("Email Of Account --> {}".format(raw[6]))
        #print("Adress Explanation --> {}".format(raw[7]))
        #print("Home Facility --> {}".format(raw[8]))
        #print("Work Facility --> {}".format(raw[9]))
        #print("Store Facility --> {}".format(raw[10]))
        #print("Panel Type --> {}".format(raw[11]))
        #print("Connection Type --> {}".format(raw[12]))
        #print("Seller --> {}".format(raw[13]))
        #print("Phone Line --> {}".format(raw[14]))
        #print("Gprs Line --> {}".format(raw[15]))
        #print("Network Line --> {}".format(raw[16]))
        #print("Montage Response --> {}".format(raw[17]))
        #print("Open Close --> {}".format(raw[18]))
        #print("Saturday Open Close --> {}".format(raw[19]))
        #print("Sunday Open Close --> {}".format(raw[20]))
        #print("GENERAL INFORMATION IS OKEY")
        conn.commit()

    except sqlite3.IntegrityError as e:
        print("Please Different ID", e)
        eel.Error_Notifications(e)

    except(Error):
        print("This is error mesafe from General Information -> {}".format(Error))
        # eel.ErrorMessage(Error)

    try:
        c = conn.cursor()
        c.execute(create_table_user_area)

        for i in range(1, userCount+1):
            #print("{} . name --> {}".format(i,user[str(i)+"name"]))
            name = user[str(i)+"name"]
            #print("{} . email --> {}".format(i,user[str(i)+"email"]))
            email = user[str(i)+"email"]
            #print("{} . password --> {}".format(i,user[str(i)+"password"]))
            password = user[str(i)+"password"]
            c.execute("INSERT INTO User_Info_Area (User_Reference_id_from_User_Section, User_Name, User_Email, User_Password, Count_Of_Users) VALUES (?, ?, ?, ?, ?)",
                      (Number_Of_Account, name, email, password, userCount))

        user_info_cursor = c.execute(
            "SELECT User_Reference_id_from_User_Section, User_Name, User_Email, User_Password, Count_Of_Users FROM User_Info_Area")
        # for i,user in enumerate(user_info_cursor):
        #print("{}. id from user info area --> {}".format(i,user[0]))
        #print("{}. User_Name from user info area --> {}".format(i,user[1]))
        #print("{}. User_Email from user info area --> {}".format(i,user[2]))
        #print("{}. User_Password from user info area --> {}".format(i,user[3]))
        #print("{}. Count  from user info area --> {}".format(i,user[4]))
        conn.commit()

    except(Error):
        print("This is Error Message from User Info DB --> {}".format(Error))
        eel.ErrorMessage(Error)

    try:
        c = conn.cursor()
        c.execute(create_table_calling_area)
        for j in range(1, countWhowillCalling+1):
            #print("{} . isim --> {}".format(j,personeWhoWillCalled[str(j)+"isim"]))
            Name_Of_Person_Who_Will_Called = personeWhoWillCalled[str(
                j)+"isim"]

            #print("{} . sifre --> {}".format(j,personeWhoWillCalled[str(j)+"sifre"]))
            Password_Of_Person_Who_Will_Called = personeWhoWillCalled[str(
                j)+"sifre"]

            #print("{} . telefon --> {}".format(j,personeWhoWillCalled[str(j)+"telefon"]))
            Telephone_Of_Person_Who_Will_Called = personeWhoWillCalled[str(
                j)+"telefon"]

            #print("{} . GSM1 --> {}".format(j,personeWhoWillCalled[str(j)+"GSM1"]))
            gsm1_Of_Person_Who_Will_Called = personeWhoWillCalled[str(
                j)+"GSM1"]

            #print("{} . GSM2 --> {}".format(j,personeWhoWillCalled[str(j)+"GSM2"]))
            gsm2_Of_Person_Who_Will_Called = personeWhoWillCalled[str(
                j)+"GSM2"]

            #print("{} . GSM3 --> {}".format(j,personeWhoWillCalled[str(j)+"GSM3"]))
            gsm3_Of_Person_Who_Will_Called = personeWhoWillCalled[str(
                j)+"GSM3"]

            c.execute("INSERT INTO User_Who_Will_Called_Stage (User_Reference_id_from_Calling_Section,Name_Of_Person_Who_Will_Called, Password_Of_Person_Who_Will_Called, Telephone_Of_Person_Who_Will_Called, gsm1_Of_Person_Who_Will_Called, gsm2_Of_Person_Who_Will_Called, gsm3_Of_Person_Who_Will_Called, Count_Person_Who_Will_Called) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                      (Number_Of_Account, Name_Of_Person_Who_Will_Called, Password_Of_Person_Who_Will_Called, Telephone_Of_Person_Who_Will_Called, gsm1_Of_Person_Who_Will_Called, gsm2_Of_Person_Who_Will_Called, gsm3_Of_Person_Who_Will_Called, countWhowillCalling))
            #print("Person Who will called Info has been added.")

        calling_person_cursor = c.execute(
            "SELECT User_Reference_id_from_Calling_Section, Name_Of_Person_Who_Will_Called, Password_Of_Person_Who_Will_Called, Telephone_Of_Person_Who_Will_Called, gsm1_Of_Person_Who_Will_Called, gsm2_Of_Person_Who_Will_Called, gsm3_Of_Person_Who_Will_Called, Count_Person_Who_Will_Called FROM User_Who_Will_Called_Stage")
        # for call in calling_person_cursor:
        #print(" ID from call db---> {}".format(call[0]))
        #print(" Name from call db---> {}".format(call[1]))
        #print(" Password from call db --> {}".format(call[2]))
        conn.commit()
    except(Error):
        #print("this is an error message from call db--> {}".format(Error))
        eel.ErrorMessage(Error)

    try:
        c = conn.cursor()
        c.execute(create_table_region_area)
        for t in range(1, regionCount+1):
            #print("{} . Bolge --> {}".format(t,Region[str(t)+"Region"]))
            region = Region[str(t)+"Region"]
            c.execute('INSERT INTO region_info_area (user_id_from_region_area, Region, Count_Of_Region) VALUES (?, ?, ?)',
                      (Number_Of_Account, region, regionCount))

        region_cursor = c.execute(
            "SELECT user_id_from_region_area, Region, Count_Of_Region FROM region_info_area")
        # for  counter,reg in enumerate(region_cursor):
        #print("{}. Region Into Database --> {} ".format(counter,reg[1]))
        #print("{}. ID Into Database --> {} ".format(counter,reg[0]))
        #print("{}. Count Into Database --> {} ".format(counter,reg[2]))

        conn.commit()
    except(Error):
        #print("this is an error message from region db--> {}".format(Error))
        eel.ErrorMessage(Error)

    c.close()
    conn.close()


@eel.expose
def check_it_out(temp_id):
    try:
        conn = sqlite3.connect('aybekler1aszDB.db')
        c = conn.cursor()
        cursor = c.execute("SELECT User_Id FROM general_Information")
        check = "False"
        print("Check is Okey ", temp_id)
        # Temp_id is string, that's why we need to convert it from string to integer.
        ids = int(temp_id)
        for i in cursor:
            print(i[0])
            temp = i[0]
            if ids == temp:
                check = "True"
                print("Check has been changed ", check)

        eel.adding(check)
        c.close()
        conn.close()

    except:
        print("Connection Error In GettingInfoFromDB")


@eel.expose
def GettingInfoFromDB():

    try:
        conn = sqlite3.connect('aybekler1aszDB.db')
        c = conn.cursor()
    except:
        print("Connection Error In GettingInfoFromDB")

    try:
        cursor = c.execute('SELECT User_Id, DATE, User_Name, User_Telephone, User_Phone, User_Address, User_Email, User_Adress_Explanation, Home_Facility_Type, Work_Facility_Type, Store_Facility_Type, Panel_Type, Connection_Type,Seller, Phone_Line, gprs, Network_Line, Montage_Responsibilities, open_close, saturday_open_close, sunday_open_close FROM general_Information')
        #  DATE, User_Name, User_Telephone, User_Phone, User_Address, User_Email, User_Adress_Explanation, Home_Facility_Type, Work_Facility_Type, Store_Facility_Type, Panel_Type, Connection_Type,Seller, Phone_Line, gprs, Network_Line, Montage_Responsibilities, open_close, saturday_open_close, sunday_open_close

        for raw in cursor:
            #print("ID --> ", raw[0])
            ID = raw[0]

            #print("DATE --> ",raw[1])
            date = raw[1]

            #print("NAME -->",raw[2])
            name = raw[2]

            #print("Telephone --> ",raw[3])
            telephone = raw[3]

            #print("PHONE --> ",raw[4])
            Phone = raw[4]

            #print("Address --> ",raw[5])
            Adress = raw[5]

            #print("Email --> ",raw[6])
            email = raw[6],

            #print("Address Aciklamasi -->",raw[7])
            adres_Explanation = raw[7]

            #print("Ev Tesis Tipi -->", raw[8])
            homeFacility = raw[8]

            #print("İs Yeri Tesis Tipi -->", raw[9])
            workPlace = raw[9]

            #print("Depo Tesis Tipi")
            store = raw[10]

            #print("Panel Tipi --> ",raw[11])
            panel = raw[11]

            #print("Baglanti Tipi -->", raw[12])
            connectionType = raw[12]

            #print("Satis Elemani -->", raw[13])
            seller = raw[13]

            #print("Telefon Hatti -->", raw[14])
            PhoneLine = raw[14]

            #print("Net hatti --> ", raw[16])
            NetLine = raw[16]

            #print("Montaj Sorumlusu -->", raw[17])
            montaj = raw[17]

            #print("Open Close -->", raw[18])
            open_close = raw[18]

            #print("Saturday -->", raw[19])
            saturday_open_close = raw[19]

            #print("Sunday -->", raw[20])
            sunday_open_close = raw[20]
            # date, name, telephone, Phone, Adress, email, adres_Explanation, homeFacility, workPlace, store, panel, connectionType, seller, PhoneLine, GPRS, NetLine, montaj, open_close, saturday_open_close, sunday_open_close
            eel.hello_js(ID, name, telephone)
    except:
        print("Showing transaction has been error in GettingInfoFromDB")
    c.close()
    conn.close()


GettingInfoFromDB()


@eel.expose
def sended(value):
    try:
        #print("this is other lib ",value)
        con = sqlite3.connect("aybekler1aszDB.db")
        c = con.cursor()
        specific_id = int(value)
        #print("specific id : ",specific_id)

    except:
        print("Error has been occupied form Connection in Sended")

    #
    try:
        cursor = c.execute("SELECT User_Id, DATE, User_Name, User_Telephone, User_Phone, User_Address, User_Email, User_Adress_Explanation, Home_Facility_Type, Work_Facility_Type, Store_Facility_Type, Panel_Type, Connection_Type,Seller, Phone_Line, gprs, Network_Line, Montage_Responsibilities, open_close, saturday_open_close, sunday_open_close  FROM general_Information Where User_Id = ? ", (specific_id,))
        for count, raw in enumerate(cursor):
            #print("--------------- {}. PERSON--------------".format(count))
            ID = raw[0]
            #print("{}. ID ---> {}".format(count,ID))
            date = raw[1]
            #print("{}. Date --> {}".format(count,date))
            name = raw[2]
            #print("{}. Name --> {}".format(count,name))
            telephone = raw[3]
            #print("{}. Telephone --> {}".format(count,telephone))
            phone = raw[4]
            #print("{}. Phone --> {}".format(count, phone))
            addres = raw[5]
            #print("{}. adress --> {}".format(count,addres))
            email = raw[6]
            #print("{}. email --> {}".format(count, email))
            adresExp = raw[7]
            #print("{}. address Explanation --> {}".format(count, adresExp))
            Home = raw[8]
            #print("{}. Home --> {}".format(count, Home))
            workPlace = raw[9]
            #print("{}. WorkPlace --> {}".format(count, workPlace))
            storage = raw[10]
            #print("{}. Storage --> {}".format(count, storage))
            paneltype = raw[11]
            #print("{}. panelType --> {}".format(count, paneltype))
            conType = raw[12]
            #print("{}. Connection type --> {}".format(count, conType))
            Seller = raw[13]
            #print("{}. Seller --> {}".format(count,Seller))
            phoneL = raw[14]
            #print("{}. Phone Line --> {}".format(count, phoneL))
            gprs = raw[15]
            #print("{}. gprs --> {}".format(count, gprs))
            networkLine = raw[16]
            #print("{}. networkLine --> {}".format(count, networkLine))
            montaj = raw[17]
            #print("{}. Montage --> {}".format(count, montaj))
            open_close = raw[18]
            #print("{}. open_close --> {}".format(count, open_close))
            saturday_open_close = raw[19]
            #print("{}. saturday_open_close --> {}".format(count, saturday_open_close))
            sunday_open_close = raw[20]
            #print("{}. sunday_open_close --> {}".format(count, sunday_open_close))
            eel.info(ID, date, name, telephone, phone, addres, email, adresExp, Home, workPlace, storage, paneltype,
                     conType, Seller, phoneL, gprs, networkLine, montaj, open_close, saturday_open_close, sunday_open_close)
            print("----------------------------------------------------\n")

    except:
        print("Error has been occupied from General Info from Sended")

    try:
        print("Id is -> ", specific_id)
        print("Type Of İd ", type(specific_id))

        user_area_cursor = c.execute(
            "SELECT User_Reference_id_from_User_Section, User_Name, User_Email, User_Password, Count_Of_Users FROM User_Info_Area WHERE User_Reference_id_from_User_Section = ?", (specific_id,))
        json_dtype_from_js_to_py = {}
        for userCount, user in enumerate(user_area_cursor):

            #print("------------------ {}. Person -----------------------------".format(userCount))
            user_area_Id = user[0]
            json_dtype_from_js_to_py[str(
                userCount)+'user_area_Id'] = user_area_Id
            #print("{}. user Id --> {}".format(userCount, user_area_Id))

            user_area_Name = user[1]
            json_dtype_from_js_to_py[str(
                userCount)+'user_area_Name'] = user_area_Name
            #print("{}. user Name --> {}".format(userCount, user_area_Name))

            user_area_email = user[2]
            json_dtype_from_js_to_py[str(
                userCount)+'user_area_email'] = user_area_email
            #print("{}. user Email --> {}".format(userCount, user_area_email))

            user_area_password = user[3]
            json_dtype_from_js_to_py[str(
                userCount)+'user_area_password'] = user_area_password
            #print("{}. user Password --> {}".format(userCount, user_area_password))

            ctf = user[4]
            json_dtype_from_js_to_py['ctf'] = ctf
            #print("{}. Count Of Users --> {}".format(userCount, ctf))
            # print("---------------------------------------------------------")
        eel.userArea(json_dtype_from_js_to_py)
    except:
        print("Error has been occupied from User Area")

    try:
        calling_user_area_cursor = c.execute("SELECT User_Reference_id_from_Calling_Section,Name_Of_Person_Who_Will_Called, Password_Of_Person_Who_Will_Called, Telephone_Of_Person_Who_Will_Called, gsm1_Of_Person_Who_Will_Called, gsm2_Of_Person_Who_Will_Called, gsm3_Of_Person_Who_Will_Called, Count_Person_Who_Will_Called FROM User_Who_Will_Called_Stage WHERE User_Reference_id_from_Calling_Section= ?", (specific_id,))
        json_dtype_from_js_to_py_from_Call = {}
        for countCall, call in enumerate(calling_user_area_cursor):
            #print("----------------- {}. Calling Area------------------------- ".format(countCall))
            call_id = call[0]
            json_dtype_from_js_to_py_from_Call[str(
                countCall)+'call_id'] = call_id
            #print(" {}. id --> {}".format(countCall, call_id))

            call_name = call[1]
            json_dtype_from_js_to_py_from_Call[str(
                countCall)+'call_name'] = call_name
            #print(" {}. Name --> {}".format(countCall, call_name))

            call_Password = call[2]
            json_dtype_from_js_to_py_from_Call[str(
                countCall)+'call_Password'] = call_Password
            #print(" {}. Password --> {}".format(countCall, call_Password))

            call_Telephone = call[3]
            json_dtype_from_js_to_py_from_Call[str(
                countCall)+'call_Telephone'] = call_Telephone
            #print(" {}. Telephone --> {}".format(countCall, call_Telephone))

            call_gsm1 = call[4]
            json_dtype_from_js_to_py_from_Call[str(
                countCall)+'call_gsm1'] = call_gsm1
            #print(" {}. GSM1 --> {}".format(countCall, call_gsm1))

            call_gsm2 = call[5]
            json_dtype_from_js_to_py_from_Call[str(
                countCall)+'call_gsm2'] = call_gsm1
            #print("{}. GSM2 --> {}".format(countCall, call_gsm2))

            call_gsm3 = call[6]
            json_dtype_from_js_to_py_from_Call[str(
                countCall)+'call_gsm3'] = call_gsm3
            #print("{}. GSM3 --> {}".format(countCall, call_gsm3))

            countcall = call[7]
            json_dtype_from_js_to_py_from_Call['countcall'] = countcall
            #print("{}. GSM3 --> {}".format(countCall, countcall))
            # print("--------------------------------------------------------------")
        eel.callArea(json_dtype_from_js_to_py_from_Call)
    except:
        print("Error has been Occupied from call Area")

    try:
        region_cursors = c.execute(
            "SELECT user_id_from_region_area, Region, Count_Of_Region FROM region_info_area WHERE user_id_from_region_area= ?", (specific_id,))
        json_dtype_from_js_to_py_from_Region = {}
        for regCount, reg in enumerate(region_cursors):
            #print("---------------------- {}. Region -----------------------------------------".format(regCount))
            reg_id = reg[0]
            json_dtype_from_js_to_py_from_Region[str(
                regCount)+'reg_id'] = reg_id
            #print("{}. id ---> {}".format(regCount, reg_id))

            region = reg[1]
            json_dtype_from_js_to_py_from_Region[str(
                regCount)+'region'] = region
            #print("{}. region ---> {}".format(regCount, region))

            regionC = reg[2]
            json_dtype_from_js_to_py_from_Region['regionC'] = regionC
            #print("{}. region ---> {}".format(regCount, regionC))
            # print("--------------------------------------------------------------------------")
        eel.regionArea(json_dtype_from_js_to_py_from_Region)
    except:
        print("Error is Occupied from region area")
    c.close()
    con.close()


@eel.expose
def Delete_Data_From_Db(id):
    try:
        con = sqlite3.connect("aybekler1aszDB.db")

        specific_id = id

        sql = "DELETE FROM general_Information WHERE User_Id = ?"
        userSql = "DELETE FROM User_Info_Area WHERE User_Reference_id_from_User_Section = ?"
        CallSql = "DELETE FROM User_Who_Will_Called_Stage WHERE User_Reference_id_from_Calling_Section = ?"
        regionSql = "DELETE FROM region_info_area WHERE user_id_from_region_area = ?"
        c = con.cursor()
        c.execute(sql, (specific_id,))
        con.commit()

        c.execute(userSql, (specific_id,))
        con.commit()

        c.execute(CallSql, (specific_id,))
        con.commit()

        c.execute(regionSql, (specific_id,))
        con.commit()

        c.close()
        con.close()
    except:
        print("Error has been occupied")


eel.start('menu.html')
