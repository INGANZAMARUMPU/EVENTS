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
		<div class="ticket" id="#ticket">
		    <div class="title">${infos.event_name}</div>
		    <div class="left">
		        <div class="img-user">
		            <img avatar src="${infos.user_img}" alt="">
		        </div>
		        <h3 firstname>${infos.firstname}</h3>
		        <h3 lastname>${infos.lastname}</h3>
		        <div class="bottom-infos">
		            <h3 phone>${infos.telephone}</h3>
		            <h5 email>${infos.email}</h5>
		        </div>
		    </div>
		    <div class="right">
		        <h3 ticket>${infos.ticket_type}</h3>
		        <div quarter>${infos.quarter}</div>
		        <div date>${infos.event_date}</div>
		        <div place>${infos.event_place}</div>
		        <div qrimage><img src="${qr}"/></div>
		    </div>
		</div>
		`
}

function generateTicket(event, ...css){
	user_card = closest(event.target, '.user-card', '.component');
	fillTicket(user_card, ...css);
}

function fillTicket(user_card, ...css){
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

	var a = window.open('', '', 'height=500, width=1000'); 
	for(let style of css){
		a.document.write(`<link rel="stylesheet" href="${style}" type="text/css" />`);
	}
	a.document.write(templateTicket(infos)); 
	a.document.close(); 
	setTimeout(function(){
		a.print();
	}, 100);
}