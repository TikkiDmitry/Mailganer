function ready() {
    alert('DOM готов');
    if(document.getElementById('checkbox1') !== null) {
        alert("hello")); // Аналог выборки и присвоения класса
    }else {
        alert("ggg")
    }
    // изображение ещё не загружено (если не было закешировано), так что размер будет 0x0
}

document.addEventListener("DOMContentLoaded", ready);



//document.addEventListener('DOMContentLoaded', function(event){ // Аналог $(document).ready(function(){
//  // Если должен быть найден один элемент
//  if(e = document.getElementById('checkbox1') !== null) {
//      alert("hello")); // Аналог выборки и присвоения класса
//  }else {
//    alert("ggg")
//  }
//});

//var checkbox = document.getElementById('checkbox');


//someCheckbox.addEventListener('change', e => {
//  if(e.target.checked === true) {
//    console.log("Checkbox is checked - boolean value: ", e.target.checked)
//  }
//if(e.target.checked === false) {
//    console.log("Checkbox is not checked - boolean value: ", e.target.checked)
//  }
//});
//checkbox.style.display = 'none'