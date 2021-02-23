
const personelCont = document.getElementById('dynamicField');
function AddPerson() {
    var container = ``;
    i = i + 1 ;
    container += `<div class="container">
    <div class="row gutters">
        <div class="card h-100">
            <div class="col-xl-9 col-lg-9 col-md-12 col-sm-12 col-12">
                <div class="card h-100">
                    <div class="card-body">
                        <div class="row gutters">
                            <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
                                <h6 class="mb-2 text-primary">Kullanıcı No ${i}:</h6>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="form-group">
                                    <label for="fullNameKullanıcıNo${i}">Kullanıcı Adı :</label>
                                    <input type="text" class="form-control" id="fullNameKullanıcıNo${i}"
                                        placeholder="Lütfen Kullanıcı Adı Giriniz">
                                </div>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="form-group">
                                    <label for="eMailKullanıcıNo4">Yetkilisi</label>
                                    <input type="text" class="form-control" id="eMailKullanıcıNo${i}"
                                        placeholder="Lütfen Yetkili Giriniz">
                                </div>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="form-group">
                                    <label for="passwordKullanıcıNo${i}">Parolası</label>
                                    <input type="password" class="form-control" id="passwordKullanıcıNo${i}"
                                        placeholder="Lütfen Parola giriniz.">
                                </div>
                            </div>
                            
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>`
personelCont.innerHTML +=container;
}



