var btns_print = document.querySelectorAll(".btn-print");
var ticket = document.getElementById("#ticket");

function closest(el, selector, stopSelector) {
  if (el.matches(selector)) return el;
  if (el.matches(stopSelector)) return null;
  return closest(el.parentNode, selector, stopSelector);
}

// btns_print.forEach(function(btn, i){
// 	btn.addEventListener('click', function (){
// 		user_card = closest(btn, '.user-card', '.component');
// 		fillTicket(user_card);
// 	});
// });

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
	ticketSelector('[avatar]').setAttribute('src', userSelector('.img-user img').getAttribute('src'));
	ticketSelector('[firstname]').textContent = userSelector('.firstname').textContent;
	ticketSelector('[lastname]').textContent = userSelector('.lastname').textContent;
	ticketSelector('[mobile]').textContent = userSelector('.mobile').textContent;
	ticketSelector('[phone]').textContent = userSelector('.phone').textContent;
	ticketSelector('[ticket]').textContent = userSelector('.tickettype').textContent;
	ticketSelector('[quarter]').textContent = userSelector('.quarter').textContent;
	ticketSelector('[date]').textContent = userSelector('.date').textContent;
	ticketSelector('[place]').textContent = userSelector('.place').textContent;
	ticketSelector('[date]').textContent = userSelector('.date').textContent;
	ticketSelector('[qrimage]').innerHTML = '';
	new QRCode(ticketSelector('[qrimage]'), {
		text: user_card.getAttribute('qr-data'),
		correctLevel: QRCode.CorrectLevel.L
	});
	var a = window.open('', '', 'height=500, width=1000'); 
	for(let style of css){
		a.document.write(`<link rel="stylesheet" href="${style}" type="text/css" />`);
	}
	setTimeout(function(){
		printable_text = document.getElementById("printable").innerHTML;
		a.document.write(printable_text); 
		a.document.close(); 
		a.print();
		a.close();
	}, 1000);
}