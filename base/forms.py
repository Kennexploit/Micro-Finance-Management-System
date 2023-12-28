from django import forms


class applicantForm(forms.Form):

	Your_name=forms.CharField(max_length=100)
	Your_id = forms.CharField(max_length=20)
	Your_contact=forms.CharField(max_length=100)
	Your_email=forms.EmailField(max_length=100)
	Amount=forms.CharField(max_length=20)
	Date = forms.CharField(max_length=20)


class AForm(forms.Form):
	Your_name = forms.CharField(max_length=100)