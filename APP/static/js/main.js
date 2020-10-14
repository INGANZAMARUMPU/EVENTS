var btns_print = document.querySelectorAll(".btn-print");
var ticket = document.getElementById("#ticket");

function closest(el, selector, stopSelector) {
  if (el.matches(selector)) return el;
  if (el.matches(stopSelector)) return null;
  return closest(el.parentNode, selector, stopSelector);
}
function templateHead(){
	return`
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title></title>
	<style type="text/css">
*{padding:0;margin:0}.container{display: inline-block;}.card{position:relative;background:#000;width:10cm;height:5cm;color:#fff;margin:2px;}.cadre1{position:absolute;border-left:2px solid #fff;border-bottom:2px solid #fff;width:2.5cm;height:2.5cm;top:1.75cm;left:1cm}.cadre2{position:absolute;border-top:2px solid #fff;border-right:2px solid #fff;width:5cm;height:3.25cm;top:1cm;left:3.75cm}.logo img{width:2.5cm}.logo{position:absolute;width:2.5cm;left:1.5cm;top:1.25cm}.alpha{position:absolute;left:1.25cm;font-size:2em;top:.25cm}.title{position:absolute;left:4.5cm;top:.5cm;font-weight:700}.qr img{width:2.5cm}.qr{position:absolute;bottom:.7cm;right:1.24cm}
	</style>
</head>
<body>
	`
}
function templateBody(infos){
	var qr = QRCode.generatePNG(infos.qr_text, {
	    ecclevel : 'L'
	});
	return`
	<div class="container">
		<div class="card">
			<div class="alpha">Alpha</div>
			<div class="title">PRIVATE PARTY</div>
			<div class="cadre1"></div>
			<div class="cadre2"></div>
			<div class="logo"><img src="${infos.logo}" alt=""/></div>
			<div class="qr"><img src="${qr}" alt=""/></div>
		</div>
	</div>
		`
}
function templateFoot(){
	return`</body></head></html>`
}
function generateTicket(event){
	user_card = closest(event.target, '.user-card', '.component');

	var userSelector = function(str){
		return user_card.querySelector(str); 
	}
	var ticketSelector = function(str){
		return ticket.querySelector(str); 
	}
	var infos = {
		event_name: "PRIVATE PARTY",
		user_img: userSelector('.img-user img').getAttribute('src'),
		firstname: userSelector('.firstname').textContent,
		lastname: userSelector('.lastname').textContent,
		telephone: userSelector('.phone').textContent,
		email: userSelector('.email').textContent,
		ticket_type: userSelector('.tickettype').textContent,
		quarter: userSelector('.quarter').textContent,
		event_date: userSelector('.date').textContent,
		event_place: userSelector('.place').textContent,
		ticket_date: userSelector('.ticket-date').textContent,
		logo: document.getElementById('logo').getAttribute('src'),
		qr_text: user_card.getAttribute('qr-data'),
	}
	printTicket(templateBody(infos));
}
function generateTickets(){
	var user_cards = document.querySelectorAll(".user-card");
	div = "";
	user_cards.forEach(function(user_card){
		var userSelector = function(str){
			return user_card.querySelector(str); 
		}
		var ticketSelector = function(str){
			return ticket.querySelector(str); 
		}
		var infos = {
			event_name: "PRIVATE PARTY",
			user_img: userSelector('.img-user img').getAttribute('src'),
			firstname: userSelector('.firstname').textContent,
			lastname: userSelector('.lastname').textContent,
			telephone: userSelector('.phone').textContent,
			email: userSelector('.email').textContent,
			ticket_type: userSelector('.tickettype').textContent,
			quarter: userSelector('.quarter').textContent,
			event_date: userSelector('.date').textContent,
			event_place: userSelector('.place').textContent,
			ticket_date: userSelector('.ticket-date').textContent,
			logo: document.getElementById('logo').getAttribute('src'),
			qr_text: user_card.getAttribute('qr-data'),
		}
		div += templateBody(infos);
	})
	printTicket(div);
}

function printTicket(text){
	var a = window.open('', '', 'height=500, width=1000'); 
	a.document.write(templateHead());  
	a.document.write(text);  
	a.document.write(templateFoot());
	setTimeout(function(){
		a.print();  
		a.close(); 
	}, 1000);
}
function toClipboard(str){
  const el = document.createElement('textarea');
  el.value = str;
  document.body.appendChild(el);
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);
}