import eel
import sqlite3

eel.init('web')

@eel.expose
def GettingInfoFromDB():
    conn = sqlite3.connect('officialed.db')
    c = conn.cursor()
    cursor = c.execute('SELECT User_Id, DATE, User_Name, User_Telephone, User_Phone, User_Address, User_Email, User_Adress_Explanation, Home_Facility_Type, Work_Facility_Type, Store_Facility_Type, Panel_Type, Connection_Type,Seller, Phone_Line, gprs, Network_Line, Montage_Responsibilities,  open_close, saturday_open_close, sunday_open_close FROM general_Information')

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

        print("Open Close -->", raw[18])
        open_close = raw[18]

        print("Saturday -->", raw[19])
        saturday_open_close = raw[19]

        print("Sunday -->", raw[20])
        sunday_open_close = raw[20]

        eel.hello_js(ID, date, name, telephone, Phone, Adress, email, adres_Explanation, homeFacility, workPlace, store, panel, connectionType, seller, PhoneLine, GPRS, NetLine, montaj, open_close, saturday_open_close, sunday_open_close)
        
    c.close()
    conn.close()
GettingInfoFromDB()
@eel.expose
def sended(value):
    try:
        print("this is other lib ",value)
        con = sqlite3.connect("officialed.db")
        c = con.cursor()
        specific_id = value
        cursor = c.execute("SELECT User_Id, DATE, User_Name, User_Telephone, User_Phone, User_Address, User_Email, User_Adress_Explanation, Home_Facility_Type, Work_Facility_Type, Store_Facility_Type, Panel_Type, Connection_Type,Seller, Phone_Line, gprs, Network_Line, Montage_Responsibilities, open_close, saturday_open_close, sunday_open_close FROM general_Information Where User_Id = ? ",(specific_id,) )
    except:
        print("Error has been occupied form Connection")

    try:
        for count,raw in enumerate(cursor):
            print("--------------- {}. PERSON--------------".format(count))
            ID = raw[0]
            print("{}. ID ---> {}".format(count,ID))
            date = raw[1]
            print("{}. Date --> {}".format(count,date))
            name = raw[2]
            print("{}. Name --> {}".format(count,name))
            telephone = raw[3]
            print("{}. Telephone --> {}".format(count,telephone))
            phone = raw[4]
            print("{}. Phone --> {}".format(count, phone))
            addres = raw[5]
            print("{}. adress --> {}".format(count,addres))
            email = raw[6]
            print("{}. email --> {}".format(count, email))
            adresExp = raw[7]
            print("{}. address Explanation --> {}".format(count, adresExp))
            Home = raw[8]
            print("{}. Home --> {}".format(count, Home))
            workPlace = raw[9]
            print("{}. WorkPlace --> {}".format(count, workPlace))
            storage = raw[10]
            print("{}. Storage --> {}".format(count, storage))
            paneltype = raw[11]
            print("{}. panelType --> {}".format(count, paneltype))
            conType = raw[12]
            print("{}. Connection type --> {}".format(count, conType))
            Seller = raw[13]
            print("{}. Seller --> {}".format(count,Seller))
            phoneL = raw[14]
            print("{}. Phone Line --> {}".format(count, phoneL))
            gprs = raw[15]
            print("{}. gprs --> {}".format(count, gprs))
            networkLine = raw[16]
            print("{}. networkLine --> {}".format(count, networkLine))
            montaj = raw[17]
            print("{}. Montage --> {}".format(count, montaj))
            open_close = raw[18]
            print("{}. open_close --> {}".format(count, open_close))
            saturday_open_close = raw[19]
            print("{}. saturday_open_close --> {}".format(count, saturday_open_close))
            sunday_open_close = raw[20]
            print("{}. sunday_open_close --> {}".format(count, sunday_open_close))
            eel.info(ID,date,name,telephone, phone, addres, email, adresExp, Home, workPlace, storage, paneltype, conType, Seller, phoneL, gprs, networkLine, montaj, open_close, saturday_open_close, sunday_open_close)
            print("----------------------------------------------------\n")
    except:
        print("Error has been occupied from General Info")

    try:
        user_area_cursor = c.execute("SELECT User_Reference_id_from_User_Section, User_Name, User_Email, User_Password, Count_Of_Users FROM User_Info_Area WHERE User_Reference_id_from_User_Section = ?",(specific_id,))
            
        for userCount,user in enumerate(user_area_cursor):
            
            print("------------------ {}. Person -----------------------------".format(userCount))
            user_area_Id = user[0]
            print("{}. user Id --> {}".format(userCount, user_area_Id))

            user_area_Name = user[1]
            print("{}. user Name --> {}".format(userCount, user_area_Name))

            user_area_email = user[2]
            print("{}. user Email --> {}".format(userCount, user_area_email))

            user_area_password = user[3]
            print("{}. user Password --> {}".format(userCount, user_area_password))

            ctf = user[4]
            print("{}. Count Of Users --> {}".format(userCount, ctf))
            print("---------------------------------------------------------")
            eel.userArea(user_area_Id, user_area_Name, user_area_email, user_area_password, ctf)
    except:
        print("Error has been occupied from User Area")

    try:
        calling_user_area_cursor = c.execute("SELECT User_Reference_id_from_Calling_Section,Name_Of_Person_Who_Will_Called, Password_Of_Person_Who_Will_Called, Telephone_Of_Person_Who_Will_Called, gsm1_Of_Person_Who_Will_Called, gsm2_Of_Person_Who_Will_Called, gsm3_Of_Person_Who_Will_Called, Count_Person_Who_Will_Called FROM User_Who_Will_Called_Stage WHERE User_Reference_id_from_Calling_Section= ?",(specific_id,))

        for countCall,call in enumerate(calling_user_area_cursor):
            print("----------------- {}. Calling Area------------------------- ".format(countCall))
            call_id = call[0]
            print(" {}. id --> {}".format(countCall, call_id))

            call_name = call[1]
            print(" {}. Name --> {}".format(countCall, call_name))

            call_Password = call[2]
            print(" {}. Password --> {}".format(countCall, call_Password))

            call_Telephone = call[3]
            print(" {}. Telephone --> {}".format(countCall, call_Telephone))

            call_gsm1 = call[4]
            print(" {}. GSM1 --> {}".format(countCall, call_gsm1))

            call_gsm2 = call[5]
            print("{}. GSM2 --> {}".format(countCall, call_gsm2))

            call_gsm3 = call[6]
            print("{}. GSM3 --> {}".format(countCall, call_gsm3))

            countcall = call[7]
            print("{}. GSM3 --> {}".format(countCall, countcall))
            print("--------------------------------------------------------------")
            eel.callArea(call_id, call_name, call_Password, call_Telephone, call_gsm1, call_gsm2, call_gsm3, countcall)
    except:
        print("Error has been Occupied from call Area")

    try:
        region_cursors = c.execute("SELECT user_id_from_region_area, Region, Count_Of_Region FROM region_info_area WHERE user_id_from_region_area= ?",(specific_id,))
    
        for regCount, reg in enumerate(region_cursors):
            print("---------------------- {}. Region -----------------------------------------".format(regCount))
            reg_id = reg[0]
            print("{}. id ---> {}".format(regCount, reg_id))

            region = reg[1]
            print("{}. region ---> {}".format(regCount, region))

            regionC = reg[2]
            print("{}. region ---> {}".format(regCount, regionC))
            print("--------------------------------------------------------------------------")
            eel.regionArea(reg_id, region, regionC)
    except :
        print("Error is Occupied from region area")
    c.close()
    con.close()
    
@eel.expose   
def Delete_Data_From_Db(id):
    try:
        con = sqlite3.connect("officialed.db")
        
        specific_id = id

        sql = "DELETE FROM general_Information WHERE User_Id = ?"
        userSql = "DELETE FROM User_Info_Area WHERE User_Reference_id_from_User_Section = ?"
        CallSql = "DELETE FROM User_Who_Will_Called_Stage WHERE User_Reference_id_from_Calling_Section = ?"
        regionSql = "DELETE FROM region_info_area WHERE user_id_from_region_area = ?"
        c = con.cursor()
        c.execute(sql,(specific_id,))
        con.commit()

        c.execute(userSql, (specific_id,))
        con.commit()

        c.execute(CallSql, (specific_id,))
        con.commit()

        c.execute(regionSql, (specific_id,))
        con.commit()


        c.close()
        con.close()
        print("Okey")

         

    
    except:
        print("Error has been occupied")
         



    


    


eel.start('Info.html')