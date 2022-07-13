// console.log("test")


// let check_btn_1 = document.getElementById('check_btn_1');
// let regis_exitoso = document.getElementById('regis_exitoso');
// let regis_no_exitoso = document.getElementById('regis_no_exitoso');

document.getElementById('regis_no_exitoso').style.visibility = "hidden"; //= true;

//check_btn_1.style.backgroundColor ="#0d6efd";
console.log('Encendido!');
function chequeo(checkbox){
    if(checkbox.checked){
        
        document.getElementById('regis_no_exitoso').style.visibility="visible";// disabled = false;
        // limpia el valor seleccionado antes de inhabilitarlo
        document.getElementById("regis_exitoso").options.item(0).selected = 'selected';
        document.getElementById('regis_exitoso').style.visibility = "hidden";
        
        
    }
    else{
        // console.log('Apagado!');
        // limpia el valor seleccionado antes de inhabilitarlo
        document.getElementById("regis_no_exitoso").options.item(0).selected = 'selected';
        document.getElementById('regis_no_exitoso').style.visibility = "hidden";
        document.getElementById('regis_exitoso').style.visibility="visible";
    }
}
