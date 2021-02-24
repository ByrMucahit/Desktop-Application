

const personelReg= document.getElementById('rowg');
function Region(){
    t = t + 1;
    var reg = ``;


    reg += ` <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
    <div class="form-group">
        <label for="${t}Region">${t}. Bölgeyi</label>
        <input type="text" class="form-control" id="${t}Region"
            placeholder="${t}. Bölgeyi Giriniz.">
    </div>
</div>`;

personelReg.innerHTML +=reg;
}