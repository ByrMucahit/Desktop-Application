function yt() {
  var data = document.getElementById("data").value
  eel.ytdownload(data)(setImage)
}



eel.expose(adding);
function adding() {
  /* Dates Values */
  var dates = document.getElementById('dates');
  var currentDate = dates.value;
  //console.log(" Dates --> " + currentDate)

  /* Account Number */
  var AccountNumber = document.getElementById('accountNo');
  var currentAccountNumber = AccountNumber.value;
  //console.log(" Account Number  --> " + currentAccountNumber)


  /* Account Name */
  var AccountName = document.getElementById('name');
  var currentAccountName = AccountName.value;
  //console.log(" Account Name  --> " + currentAccountName);

  /* Telephone */
  var AccountTelephone = document.getElementById('telPhone');
  var currentAccountTelephone = AccountTelephone.value;
  //console.log(" Account Telephone  --> " + currentAccountTelephone);

  /* Phone */
  var AccountPhone = document.getElementById('Phone');
  var currentAccountPhone = AccountPhone.value;
  //console.log(" Account Phone  --> " + currentAccountPhone);

  /* Adress */
  var AccountAdress = document.getElementById('adress');
  var currentAccountAdress = AccountAdress.value;
  //console.log(" Account Adress  --> " + currentAccountAdress);

  /* Email */
  var AccountEmail = document.getElementById('email');
  var currentAccountEmail = AccountEmail.value;
  //console.log(" Account Email  --> " + currentAccountEmail);

  /* Explanation Of Adress */
  var AccountExp = document.getElementById('expAdres');
  var currentAccountAdressExp = AccountExp.value;
 // console.log(" Account Explanation  --> " + currentAccountAdressExp);


  /* CheckBox */
  var  home = document.getElementById("Ev");
  var workPlace = document.getElementById('IsYeri');
  var Depo = document.getElementById('depo');
  
  //console.log("Home -->" + home.value+ "\nworkPlace --> " + workPlace.value+ "\n Depo--> " + Depo.value );
  

  /* Type Of Panel */
  var typeOfPanel = document.getElementById('panelInp');
  var currentPanelType = typeOfPanel.value;
  //console.log("Panel Tipi --> "+ currentPanelType); 


  /* Type Of Connections */
  var typeoOfConnection = document.getElementById('panelCon');
  var currentTypeOfConnection = typeoOfConnection.value;
  //console.log("Bağlantı Tipi --> "+ currentTypeOfConnection);

  /* Selling Personel */
  var SellingPersonel = document.getElementById('sellingPerso');
  var currentSellingPersonel = SellingPersonel.value;
  //console.log("Satış Elemanı --> "+ currentSellingPersonel);

   /* Line Of Telephone */
   var LineoFtelephone = document.getElementById('lineOfTel');
   var currentLineoFtelephone = LineoFtelephone.value;
   //console.log("Tel Hattı --> "+ currentLineoFtelephone);

   
   /* GPRS */
   var GPRS = document.getElementById('gprs');
   var currentGPRS = GPRS.value;
   //console.log("GPRS --> "+ currentGPRS);

 /* Net Line */
 var netLine = document.getElementById('lineOfNet');
 var currentnetLine = netLine.value;
 //console.log("Net Line --> "+ currentnetLine);

 /* INSTALLATION MANAGER */ 
 var InstManager = document.getElementById('installationManag');
 var currentnetInstManager = InstManager.value;
 //console.log("Instalation Manager --> "+ currentnetInstManager);



 /* USERS */
 
 /* USER 1 */
 var user1Name = document.getElementById("fullNameKullanıcıNo1");
 var user1Email = document.getElementById("eMailKullanıcıNo1");
 var user1Password = document.getElementById("passwordKullanıcıNo1");

 //console.log("1. user name --> "+ user1Name.value + "\n 1. user email --> "+ user1Email.value + "\n 1. user password --> "+ user1Password);

 /* USER 2 */
 var user2Name = document.getElementById("fullNameKullanıcıNo2");
 var user2Email = document.getElementById("eMailKullanıcıNo2");
 var user2Password = document.getElementById("passwordKullanıcıNo2");

 //console.log("2. user name --> "+ user2Name.value + "\n 2. user email --> "+ user2Email.value + "\n 2. user password --> "+ user2Password);

/* USER 3 */
var user3Name = document.getElementById("fullNameKullanıcıNo3");
var user3Email = document.getElementById("eMailKullanıcıNo3");
var user3Password = document.getElementById("passwordKullanıcıNo3");

//console.log("3. user name --> "+ user3Name.value + "\n 3. user email --> "+ user3Email.value + "\n 3. user password --> "+ user3Password);

/* USER 4 */
var user4Name = document.getElementById("fullNameKullanıcıNo4");
var user4Email = document.getElementById("eMailKullanıcıNo4");
var user4Password = document.getElementById("passwordKullanıcıNo4");

//console.log("4. user name --> "+ user4Name.value + "\n 4. user email --> "+ user4Email.value + "\n 4. user password --> "+ user4Password);



/* Calling In Case Of Alert */

/* Calling Person 1 */
var user1CallingName = document.getElementById("fullNameAranacakKisi1");
//console.log(" name Calling user 1 -> "+ user1CallingName.value )
var user1CallingPassword = document.getElementById("passowdAranacakKisi1");
//console.log(" name Calling pass 1 -> "+ user1CallingPassword.value)
var user1CallingHomeTel = document.getElementById("phoneAranacakKisi1");
//console.log(" name Calling Home Tel 1 -> "+ user1CallingHomeTel.value)
var user1CallingGSM1 = document.getElementById("GSM1AranacakKisi1");
//console.log(" name Calling GSM Tel 1 -> "+ user1CallingGSM1.value)
var user1CallingGSM2 = document.getElementById("GSM2AranacakKisi1");
//console.log(" name Calling GSM Tel 2 -> "+ user1CallingGSM2.value)
var user1CallingGSM3 = document.getElementById("GSM3AranacakKisi1");
//console.log(" name Calling GSM Tel 3-> "+ user1CallingGSM3.value)

/* Calling Person 2 */
var user2CallingName = document.getElementById("fullNameAranacakKisi2");
//console.log(" name Calling user 2 -> "+ user2CallingName.value )
var user2CallingPassword = document.getElementById("passowdAranacakKisi2");
//console.log(" name Calling pass 2 -> "+ user2CallingPassword.value)
var user2CallingHomeTel = document.getElementById("phoneAranacakKisi2");
//console.log(" name Calling Home Tel 2 -> "+ user1CallingHomeTel.value)
var user2CallingGSM1 = document.getElementById("GSM1AranacakKisi2");
//console.log(" name Calling GSM Tel 1 -> "+ user2CallingGSM1.value)
var user2CallingGSM2 = document.getElementById("GSM2AranacakKisi2");
//console.log(" name Calling GSM Tel 2 -> "+ user2CallingGSM2.value)
var user2CallingGSM3 = document.getElementById("GSM3AranacakKisi2");
//console.log(" name Calling GSM Tel 3-> "+ user2CallingGSM3.value)



/* Calling Person 3 */
var user3CallingName = document.getElementById("fullNameAranacakKisi3");
//console.log(" name Calling user 3 -> "+ user3CallingName.value )
var user3CallingPassword = document.getElementById("passowdAranacakKisi3");
//console.log(" name Calling pass 3 -> "+ user3CallingPassword.value)
var user3CallingHomeTel = document.getElementById("phoneAranacakKisi3");
//console.log(" name Calling Home Tel 3 -> "+ user3CallingHomeTel.value)
var user3CallingGSM1 = document.getElementById("GSM1AranacakKisi3");
//console.log(" name Calling GSM Tel 1 -> "+ user3CallingGSM1.value)
var user3CallingGSM2 = document.getElementById("GSM2AranacakKisi3");
//console.log(" name Calling GSM Tel 2 -> "+ user3CallingGSM2.value)
var user3CallingGSM3 = document.getElementById("GSM1AranacakKisi3");
//console.log(" name Calling GSM Tel 3-> "+ user3CallingGSM3.value)


/* Calling Person 4 */
var user4CallingName = document.getElementById("fullNameAranacakKisi4");
//console.log(" name Calling user 3 -> "+ user4CallingName.value )
var user4CallingPassword = document.getElementById("passowdAranacakKisi4");
//console.log(" name Calling pass 3 -> "+ user4CallingPassword.value)
var user4CallingHomeTel = document.getElementById("phoneAranacakKisi4");
//console.log(" name Calling Home Tel 4 -> "+ user4CallingHomeTel.value)
var user4CallingGSM1 = document.getElementById("GSM1AranacakKisi4");
//console.log(" name Calling GSM Tel 1 -> "+ user4CallingGSM1.value)
var user4CallingGSM2 = document.getElementById("GSM2AranacakKisi4");
//console.log(" name Calling GSM Tel 2 -> "+ user4CallingGSM2.value)
var user4CallingGSM3 = document.getElementById("GSM1AranacakKisi4");
//console.log(" name Calling GSM Tel 3-> "+ user4CallingGSM3.value)


/* Desire that Open up / Close up */
var Open = document.getElementById("flexRadioDefault1")
var close = document.getElementById("flexRadioDefault2")
var which= null;
if(Open.checked === true ){
  which = Open.value
}else if( close.checked === true){
  which = close.value
}

/* Weekend */
var weekend_first_day = document.getElementById("inlineCheckbox4");
var weekend_second_Day = document.getElementById("inlineCheckbox5");
var weekEnd = {"Cumatesi":"Hayir","Pazar":"Hayir"};
if( weekend_first_day.checked === true){
  weekEnd['Cumatesi']="Evet"
}
if( weekend_second_Day.checked === true){
  weekEnd['Pazar']="Evet"




/* <!------------------------------------------------Dedector Distribution And Memory------------------------------------------------------> */
var firstRegion = document.getElementById("firstRegion");
//console.log("1. Bölge --> "+ firstRegion.value);

var secondRegion = document.getElementById("seconRegion");
//console.log("2. Bölge --> "+ secondRegion.value);

var thirRegion = document.getElementById("thirRegion");
//console.log("3. Bölge --> "+ thirRegion.value);

var fourthRegion = document.getElementById("fourthRegion");
//console.log("4. Bölge --> "+ fourthRegion.value);

var fifthRegion = document.getElementById("fifthRegion");
//console.log("5. Bölge --> "+ fifthRegion.value);

var sixthRegion = document.getElementById("sixthRegion");
//console.log("6. Bölge --> "+ sixthRegion.value);

var seventhRegion = document.getElementById("seventhRegion");
//console.log("7. Bölge --> "+ seventhRegion.value);

var eigthRegion = document.getElementById("eigthRegion");
//console.log("8. Bölge --> "+ eigthRegion.value);
 
var ninthRegion = document.getElementById("ninthRegion");
//console.log("9. Bölge --> "+ ninthRegion.value);

var tenthRegion = document.getElementById("tenthRegion");
//console.log("10. Bölge --> "+ tenthRegion.value);

var eleventhRegion = document.getElementById("eleventhRegion");
/*console.log("11. Bölge --> "+ eleventhRegion.value);*/

var twelvethRegion = document.getElementById("twelvethRegion");
/*console.log("12. Bölge --> "+ twelvethRegion.value);*/

/* JSON */
var user={};
var call={};
var region ={};
var list = [];



/* Get Dynamic  Elements  from Personel*/

/* Static */
/*--------USER - 1 ------------- */
user[1+"id"]=user1Name;
user[1+"email"]= user1Email;
user[1+"password"]= user1Password;   
/*--------USER - 2 ------------- */
user[2+"id"]=user2Name;
user[2+"email"]= user2Email;
user[2+"password"]= user2Password;   
/*--------USER - 3 ------------- */
user[3+"id"]=user3Name;
user[3+"email"]= user3Email;
user[3+"password"]= user3Password;   


/* Dynamic */
$('input').each(function(input){
  for(var n= 1; n<i+1;n++)
  {
    var value = $(this).val();
    var id = $(this).attr('id');
    if( id === "fullNameKullanıcıNo"+n)
    {
      if(n >=4){
        
      }
     var pers = $('#eMailKullanıcıNo'+n).val();
     var pss = $('#passwordKullanıcıNo'+n).val();
      console.log('id: ' + id + ' value:' + value + "\n resp --->"+ pers + " password -->" + pss);
        
      user[n+"id"]=id;
      user[n+"email"]= pers;
      user[n+"password"]= pss;   
    }
  }
})

for (var s = 1 ; s< i+1; s++){
/*console.log("this list ; \n "+"id : "+user[s+"id"] +"\n"+"email :"+user[s+"email"]+"\n"+"password :"+user[s+"password"])*/
}



var user1CallingName = document.getElementById("fullNameAranacakKisi1");
/*console.log(" name Calling user 1 -> "+ user1CallingName.value )*/
var user1CallingPassword = document.getElementById("passowdAranacakKisi1");
/*console.log(" name Calling pass 1 -> "+ user1CallingPassword.value)*/
var user1CallingHomeTel = document.getElementById("phoneAranacakKisi1");
/*console.log(" name Calling Home Tel 1 -> "+ user1CallingHomeTel.value)*/
var user1CallingGSM1 = document.getElementById("GSM1AranacakKisi1");
/*console.log(" name Calling GSM Tel 1 -> "+ user1CallingGSM1.value)*/
var user1CallingGSM2 = document.getElementById("GSM2AranacakKisi1");
/*console.log(" name Calling GSM Tel 2 -> "+ user1CallingGSM2.value)*/
var user1CallingGSM3 = document.getElementById("GSM3AranacakKisi1");
/*console.log(" name Calling GSM Tel 3-> "+ user1CallingGSM3.value)*/

/* Get Dynamic  Elements  from Calling Person*/

/* Static */
/*--------USER - 1 ------------- */
call[1+"isim"]=user1CallingName.value;
call[1+"sifre"]= user1CallingPassword.value;
call[1+"telefon"]= user1CallingHomeTel.value; 
call[1+"GSM1"]= user1CallingGSM1.value;   
call[1+"GSM2"]=  user1CallingGSM2.value;   
call[1+"GSM3"]=  user1CallingGSM3.value;  
/*--------USER - 2 ------------- */
call[2+"isim"]=user2CallingName.value;
call[2+"sifre"]= user2CallingPassword.value;
call[2+"telefon"]= user2CallingHomeTel.value; 
call[2+"GSM1"]= user2CallingGSM1.value;   
call[2+"GSM2"]=  user2CallingGSM2.value;   
call[2+"GSM3"]=  user2CallingGSM3.value;  
/*--------USER - 3 ------------- */
call[3+"isim"]=user3CallingName.value;
call[3+"sifre"]= user3CallingPassword.value;
call[3+"telefon"]= user3CallingHomeTel.value; 
call[3+"GSM1"]= user3CallingGSM1.value;   
call[3+"GSM2"]=  user3CallingGSM2.value;   
call[3+"GSM3"]=  user3CallingGSM3.value;  

/*--------USER - 4 ------------- 
call[4+"isim"]=user4CallingName.value;
call[4+"sifre"]= user4CallingPassword.value;
call[4+"telefon"]= user4CallingHomeTel.value; 
call[4+"GSM1"]= user4CallingGSM1.value;   
call[4+"GSM2"]=  user4CallingGSM2.value;   
call[4+"GSM3"]=  user4CallingGSM3.value; */

$('input').each(function(input){
  for(var l= 4; l<m+1;l++)
  {
    var value = $(this).val();
    var id = $(this).attr('id');
    if( id === "fullNameAranacakKisi"+l)
    {
    call[l+"isim"]= value;
    call[l+"telefon"]= $('#phoneAranacakKisi1'+l).val();
    call[l+"sifre"] = $('#passowdAranacakKisi'+l).val();
    call[l+"GSM1"]= $('#GSM1AranacakKisi'+l).val();
    call[l+"GSM2"]= $('#GSM2AranacakKisi'+l).val();
    call[l+"GSM3"]= $('#GSM3AranacakKisi'+l).val();  
    }  
  } 
})
/*for (var rootCall = 1 ; rootCall< m+1; rootCall++){
  console.log("Calling"+rootCall+"\n"+"isim : "+call[rootCall+"isim"] +"\n"+"telefon :"+call[rootCall+"telefon"]+"\n"+"sifre :"+call[rootCall+"sifre"]+"\n"+"GSM1: "+call[rootCall+"GSM1"]+"\n GSM2 : "+call[rootCall+"GSM1"]+"\n GSM 3 :"+call[rootCall+"GSM3"])
  }*/



/* Open/Close*/



/* Get  Elements  from Region*/
/* Static */
/*--------Regions ------------- */
region[1+"Region"]=firstRegion.value;
region[2+"Region"]=secondRegion.value;
region[3+"Region"]=thirRegion.value; 
region[4+"Region"]=fourthRegion.value;
region[5+"Region"]=fifthRegion.value;
region[6+"Region"]=sixthRegion.value;
region[7+"Region"]=seventhRegion.value;
region[8+"Region"]=eigthRegion.value; 
region[9+"Region"]=ninthRegion.value;
region[10+"Region"]=tenthRegion.value;  
region[11+"Region"]=eleventhRegion.value;
region[12+"Region"]=twelvethRegion.value; 


/* Dynamic */

$('input').each(function(input){
  for(var rootreg= 13; rootreg<=t+1;rootreg++)
  {
    var value = $(this).val();
    var id = $(this).attr('id');
    if( id === rootreg+"Region")
    {
      region[rootreg+"Region"]=value;   
    }  
  } 
})

/*for (var rootr = 1 ; rootr< t+1; rootr++){
  console.log("Region"+ rootr+"-->"+region[rootr+"Region"] )
  }*/

var  home = document.getElementById("Ev");
var workPlace = document.getElementById('IsYeri');
var Depo = document.getElementById('depo');
/* JSON TYPES */
var user={};
var call={};
var region ={};
text = { 
  "date": currentDate,
   "AboneNo":currentAccountNumber,
  "AboneAdı": currentAccountName,
  "AboneTelefon":currentAccountTelephone,
  "AboneCepTelefon":currentAccountPhone,
  "AboneAdress":currentAccountAdress,
  "AboneEmail":currentAccountEmail,
  "AboneAdresAciklamasi":currentAccountAdressExp,
 "EvTesisTipi":home.value,
 "Isyeri:":workPlace.value,
 "Depo":Depo.value,
 "PanelTipi":currentPanelType,
 "BağlantıTipi":currentTypeOfConnection,
 "SatisPersoneli":currentSellingPersonel,
 "TelefonHatti":currentLineoFtelephone,
 "GPRS":currentGPRS,
 "InternetHatti":currentnetLine,
"MontajSorumlusu":currentnetInstManager,
"Kullanıcılar":user,
"AranacakKisiler":call,
"Acik_Kapali":which,
"HaftasonuHizmet":weekEnd,
"Bölgeler":region
}
var userInfo = JSON.stringify(text);
eel.hellopython(('Running python function from ajvascript side') (function(ret){console.log(ret)}))
/*console.log("date --> "+text.date + "\nAbone No ---> "+currentAccountNumber+ "\n Abone Adı --> "+currentAccountName+ "\n AboneTelefon --> " +currentAccountTelephone)*/

}}
