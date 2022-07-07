// console.log("test")


// let check_btn_1 = document.getElementById('check_btn_1');
// let regis_exitoso = document.getElementById('regis_exitoso');
// let regis_no_exitoso = document.getElementById('regis_no_exitoso');

document.getElementById('regis_no_exitoso').disabled = true;

//check_btn_1.style.backgroundColor ="#0d6efd";

function chequeo(checkbox){
    if(checkbox.checked){
        // console.log('Encendido!');
        document.getElementById('regis_no_exitoso').disabled = false;
        // limpia el valor seleccionado antes de inhabilitarlo
        document.getElementById("regis_exitoso").options.item(0).selected = 'selected';
        document.getElementById('regis_exitoso').disabled = true;
    }
    else{
        // console.log('Apagado!');
        // limpia el valor seleccionado antes de inhabilitarlo
        document.getElementById("regis_no_exitoso").options.item(0).selected = 'selected';
        document.getElementById('regis_no_exitoso').disabled = true;
        document.getElementById('regis_exitoso').disabled = false;
    }
}
