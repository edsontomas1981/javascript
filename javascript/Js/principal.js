/*
a = ai
e = enter
i = imes
o = ober
u = ufat
*/


var btnCriptografar = document.querySelector("#btn-cripto");
var txtCripto = document.querySelector("#input-texto");
var	btnLiga = document.querySelector("#btn-liga");
var msg = document.querySelector("#msg")
var msgCripto = "";

txtCripto.addEventListener("keypress",function(evento){

	
	var tecla = evento.key;

	msgCripto = msgCripto + trocaVogais(tecla);

	console.log(msgCripto);


})
/*btnCriptografar.addEventListener("click",function(evento){

	evento.preventDefault();

	if(!automatico){
	
		btnCriptografar.classList.add("btn-automatico-on");

		automatico = true;

		console.log(btnLiga.checked)

		
	}else{

		btnCriptografar.classList.remove("btn-automatico-on");

		automatico = false;

		console.log(btnLiga.checked)
	}


})*/
