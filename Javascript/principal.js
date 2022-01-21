var btnCriptografar = document.querySelector(".btn-criptografar");
var txtCripto = document.querySelector(".texto-entrada");
var	btnLiga = document.querySelector(".info-check");
var msg = document.querySelector(".texto-saida")
var btnDescripto = document.querySelector(".btn-descriptografar");
var btnCopiar = document.querySelector(".btn-copiar");
var msgCripto = "";

limpaCampos()

btnLiga.addEventListener("click",function(evento){

	evento.preventDefault ; 

	limpaCampos()
})

btnCopiar.addEventListener("click",function(evento){

	evento.preventDefault();

	copiaTexto(msg)
})

btnDescripto.addEventListener("click",function(evento){

	evento.preventDefault();

	msgCripto = txtCripto.value

	msg.value=descriptografa(msgCripto)
})

txtCripto.addEventListener("keypress",function(evento){

	if (btnLiga.checked){

		var tecla = evento.key;

		msgCripto = msgCripto + criptografa(tecla);

		msg.value = msgCripto
	}
})

btnCriptografar.addEventListener("click",function (evento){

	var letras = txtCripto.value.split("");

	evento.preventDefault();

	msgCripto = ""

	msg.value = "";

	for (var i = 0; i < letras.length; i++) {

		msgCripto = msgCripto + criptografa(letras[i]);

		msg.value = msgCripto
	}
})