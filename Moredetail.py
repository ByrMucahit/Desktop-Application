import eel
import sqlite3


eel.init('web')

def GettingDetailInfoFromDB():
    con = sqlite3.connect("official.db")
    c = con.cursor()
    specific_id = 8989898
    cursor = c.execute("SELECT User_Id, DATE, User_Name, User_Telephone, User_Phone, User_Address, User_Email, User_Adress_Explanation, Home_Facility_Type, Work_Facility_Type, Store_Facility_Type, Panel_Type, Connection_Type,Seller, Phone_Line, gprs, Network_Line, Montage_Responsibilities, open_close, saturday_open_close, sunday_open_close FROM general_Information Where User_Id = ? ",(specific_id,) )
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

        Open_Close = raw[18]
        print("{}. Open_Close --> {}".format(count, Open_Close))
        saturday_close_open = raw[19]
        print("{}. saturday_close_open --> {}".format(count, saturday_close_open))
        sunday_close_open = raw[20]
        print("{}. sunday_close_open --> {}".format(count, sunday_close_open))
        eel.info(ID,date,name,telephone, phone, addres, email, adresExp, Home, workPlace, storage, paneltype, conType, Seller, phoneL, gprs, networkLine, montaj, Open_Close, saturday_close_open, sunday_close_open)
        print("----------------------------------------------------\n")
    
    user_area_cursor = c.execute("SELECT User_Reference_id_from_User_Section, User_Name, User_Email, User_Password FROM User_Info_Area WHERE User_Reference_id_from_User_Section = ?",(specific_id,))

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
        print("---------------------------------------------------------")
        eel.userArea(user_area_Id, user_area_Name, user_area_email, user_area_password)
    
    calling_user_area_cursor = c.execute("SELECT User_Reference_id_from_Calling_Section,Name_Of_Person_Who_Will_Called, Password_Of_Person_Who_Will_Called, Telephone_Of_Person_Who_Will_Called, gsm1_Of_Person_Who_Will_Called, gsm2_Of_Person_Who_Will_Called, gsm3_Of_Person_Who_Will_Called FROM User_Who_Will_Called_Stage WHERE User_Reference_id_from_Calling_Section= ?",(specific_id,))

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
        print("--------------------------------------------------------------")
        eel.callArea(call_id, call_name, call_Password, call_Telephone, call_gsm1, call_gsm2, call_gsm3)
    region_cursors = c.execute("SELECT user_id_from_region_area, Region FROM region_info_area WHERE user_id_from_region_area= ?",(specific_id,))
    
    for regCount, reg in enumerate(region_cursors):
        print("---------------------- {}. Region -----------------------------------------".format(regCount))
        reg_id = reg[0]
        print("{}. id ---> {}".format(regCount, reg_id))

        region = reg[1]
        print("{}. region ---> {}".format(regCount, region))
        print("--------------------------------------------------------------------------")
        eel.regionArea(reg_id, region)
    cursor.close()
    con.close()
    
    
    
    


    


    
    
def whatever(sel):
    print("Selling -->",sel)
        
        
    

    
    

    

GettingDetailInfoFromDB()




eel.start('PersonalityInfo.html')