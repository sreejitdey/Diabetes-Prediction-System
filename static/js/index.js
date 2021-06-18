var currentTab = 0;

showTab(currentTab);

function validateForm() {
	var x, y1, y2, i, valid = true;
	x = document.getElementsByClassName("row");
	y1 = x[currentTab].getElementsByTagName("select");
	y2 = x[currentTab].getElementsByTagName("input");
	for (i = 0; i < y1.length; i++) {
		if (y1[i].value == "") {
			valid = false;
			break;
		}
	}
	for (i = 0; i < y2.length; i++) {
		if (y2[i].value == "") {
			valid = false;
			break;
		}
	}
	return valid;
}

function showTab(n) {
	var x = document.getElementsByClassName("row");
	x[n].style.display = "flex";
	if (n == x.length - 1)
		document.getElementById("predictBtn").innerHTML = "Predict";
	else
		document.getElementById("predictBtn").innerHTML = "Next";
}

function nextRow(n) {
	var x = document.getElementsByClassName("row");
	if (n == 1 && !validateForm())
		return false;
	x[currentTab].style.display = "none";
	currentTab = currentTab + n;
	if (currentTab >= x.length) {
		document.body.style.display = "none";
		document.getElementById("home").submit();
		document.getElementById("home").action = "/predict";
		return false;
	}
	showTab(currentTab);
}
