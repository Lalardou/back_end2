$(document).ready(function () {

    $("#form1").submit(function (e) {
        e.preventDefault();
        let mensajeEnviar = "";
        let entrar = false;
        var nomb = $("#nom").val();

        if(nomb.trim().length < 4  ||  nomb.trim().length > 7){
            mensajeEnviar += "La longitud no es correcta<br>";
            entrar = true;
        }

        var letra = nomb.charAt(0);
        if(!esMayuscula(letra)){
            mensajeEnviar += "La primera letra es minúscula<br>";
            entrar = true;
        }

        if(entrar){
            $("#mensajes").html(mensajeEnviar);
        }
        else{
            $("#mensajes").html("Formulario Enviado");
        }


    });

    function esMayuscula(letra){
        return letra == letra.toUpperCase();
    }
})
