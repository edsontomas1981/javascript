
function criptografa(letra) {
	
	switch (letra) {
	  case "a":
	  	return "ai"
	    break;
	  case "e":
	    return "enter";
		break;
	  case "i":
	    return "imes";
		break;
	  case "o":
	    return "ober";
		break;
	  case "u":
		return "ufat";
		break;  	
	  default:
	  	return letra
	  	break;
	}



}

function copiaTexto(campoTexto) {

    campoTexto.select();
    campoTexto.setSelectionRange(0, 99999)
    document.execCommand("copy");
    alert("O texto é copiado : " + campoTexto.value);
}

function limpaCampos (){
	txtCripto.value = '';
	msg.value = '';
	msgCripto = ''
}

function descriptografa(texto){

	var texto_desc = texto.replace(/ai/g, 'a');

	texto_desc = texto_desc.replace(/enter/g, 'e');

	texto_desc = texto_desc.replace(/imes/g, 'i');

	texto_desc = texto_desc.replace(/ober/g, 'o');

	texto_desc = texto_desc.replace(/ufat/g, 'u');

	return texto_desc

}

