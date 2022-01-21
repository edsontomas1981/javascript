var btnCriptografar = document.querySelector("#btn-criptografar");
var txtCripto = document.querySelector("#texto-saida");
var	btnLiga = document.querySelector("#info-check");
var msg = document.querySelector("#texto-saida")
var msgCripto = "";

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

	for (var i = 0; i < letras.length; i++) {

		msgCripto = msgCripto + criptografa(letras[i]);

		msg.value = msgCripto
	}
})