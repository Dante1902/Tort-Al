function ShowMenu(){
	var menu = document.getElementsByClassName('hidden-menu')[0];
	if (menu.style.visibility == "hidden"){
		menu.style.visibility = "visible";
	}

	else{
		menu.style.visibility = "hidden";
	}
}

function Subscribe(){


	var push = document.getElementsByClassName('push')[0];
	var mail = document.form_email.email.value;

	if (mail != ""){
		push.style.visibility = "visible";
		push.classList.add("fadeInUp");
	}

	document.form_email.email.value = "";

	// обработка

	setTimeout(function(){
		push.classList.remove("fadeInUp");
		push.classList.add("fadeOutDown");
		setTimeout(function(){
			push.style.visibility = "hidden";
			push.classList.remove("fadeOutDown");
		}, 1000);
	}, 10000);
}