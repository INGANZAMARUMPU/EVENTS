var btns_print = document.querySelectorAll(".btn-print");
var ticket = document.getElementById("#ticket");

function closest(el, selector, stopSelector) {
  if (el.matches(selector)) return el;
  if (el.matches(stopSelector)) return null;
  return closest(el.parentNode, selector, stopSelector);
}

function templateTicket(infos){
	var qr = QRCode.generatePNG(infos.qr_text, {
	    ecclevel : 'L'
	});
	return`
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title></title>
	<style type="text/css" media="screen">
		*{
			padding: 0;
			margin: 0;
		}
		.card{
			position: relative;
			background: black;
			width: 10cm;
			height: 5cm;
			color: white;
		}
		.cadre1{
			position: absolute;
			border-left: 2px solid white;
			border-bottom: 2px solid white;
			width: 2.5cm;
			height: 2.5cm;
			top: 1.75cm;
			left: 1cm;
		}
		.cadre2{
			position: absolute;
			border-top: 2px solid white;
			border-right: 2px solid white;
			width: 5cm;
			height: 3.25cm;
			top:1cm;
			left: 3.75cm;
		}
		.logo img{
			width: 2.5cm;
		}
		.logo{
			position: absolute;
			width: 2.5cm;
			left: 1.5cm;
			top: 1.25cm;
		}
		.alpha{
			position: absolute;
			left:1.25cm;
			font-size: 2em;
			top: 0.25cm;
		}
		.title{
			position: absolute;
			left: 4.5cm;
			top: 0.5cm;
			font-weight: bold;
		}
		.qr img{
			width: 2.5cm;
		}
		.qr{
			position: absolute;
			bottom: 0.7cm;
			right: 1.24cm;
		}
	</style>
</head>
<body>
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
</body>
		`
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
	printTicket(templateTicket(infos));
}
function generateTickets(){
	var user_cards = document.querySelectorAll(".user-card");
	div = `<div style="display: inline-flex;">`;
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
			qr_text: user_card.getAttribute('qr-data'),
		}
		div += templateTicket(infos);
	})
	div += "</div>"
	printTicket(div);
}

function printTicket(text){
	var a = window.open('', '', 'height=500, width=1000'); 
	a.document.write(text);  
	a.document.close(); 
	setTimeout(function(){
		a.print();
	}, 100);
}
function toClipboard(str){
  const el = document.createElement('textarea');
  el.value = str;
  document.body.appendChild(el);
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);
}