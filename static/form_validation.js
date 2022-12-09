
// Survey form input validation

const formCheck = () => {
	const form = document.getElementById('survey-form');
	const formData = new FormData(form);
	if ([...formData].length == 11) {
		form.submit();
	} else {
		alert('Please answer all questions.');
	}
};
