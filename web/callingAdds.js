

const personelCall = document.getElementById('dynamicCall');
function addCallingPerson() {
    console.log("Hello from call");

    var container = ``;
    m = m + 1 ;
    container += `<div class="container">
    <div class="row gutters">
        <div class="card h-100">
            <div class="col-xl-9 col-lg-9 col-md-12 col-sm-12 col-12">
                <div class="card h-100">
                    <div class="card-body">
                        <div class="row gutters">
                            <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
                                <h6 class="mb-2 text-primary">Aranacak Kişi ${m}:</h6>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="form-group">
                                    <label for="fullNameAranacakKisi${m}">Adı Soyadı :</label>
                                    <input type="text" class="form-control" id="fullNameAranacakKisi${m}"
                                        placeholder="Lütfen Ad ve Soyad Giriniz...">
                                </div>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="form-group">
                                    <label for="passowdAranacakKisi${m}">Password:</label>
                                    <input type="password" class="form-control" id="passowdAranacakKisi${m}"
                                        placeholder="Lütfen Şifre Giriniz">
                                </div>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="form-group">
                                    <label for="phoneAranacakKisi${m}">Ev Tel</label>
                                    <input type="tel" class="form-control" id="phoneAranacakKisi${m}"
                                        placeholder="Lütfen Ev Telefonu giriniz.">
                                </div>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="form-group">
                                    <label for="GSM1AranacakKisi${m}">GSM-1</label>
                                    <input type="tel" class="form-control" id="GSM1AranacakKisi${m}"
                                        placeholder="Telefon Numrasaı Giriniz.">
                                </div>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="form-group">
                                    <label for="GSM2AranacakKisi${m}">GSM-2</label>
                                    <input type="tel" class="form-control" id="GSM2AranacakKisi${m}"
                                        placeholder="Telefon Numrasaı Giriniz.">
                                </div>
                            </div>

                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="form-group">
                                    <label for="GSM3AranacakKisi${m}">GSM-3</label>
                                    <input type="tel" class="form-control" id="GSM3AranacakKisi${m}"
                                        placeholder="Telefon Numrasaı Giriniz.">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
    </div>
    
</div>`
personelCall.innerHTML +=container;
}
