from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . forms import applicantForm, AForm
from django.contrib import messages
from . models import applicant



def index(request):
	return render(request,'index.html')


def login_view(request):
	
 	if request.method=='POST':
 		form = AuthenticationForm(request, data=request.POST)
 		if form.is_valid(): 
 			user = form.get_user()
 			login(request, user)
 			return redirect('/loan')
 	else: 
 		form = AuthenticationForm(request)
 		context = { "form": form}
 		return render(request, 'login.html', context)



def logout_view(request):
	if request.method=='POST':
		logout(request)
		return redirect('/')
	return render(request, 'logout.html')

def register_view(request):
	form=UserCreationForm(request.POST or None)
	if form.is_valid():
		user_obj = form.save()
		return redirect('/login')
	context = {"form": form}
	return render(request, 'register.html', context)
 





def Loan(request):
	form =applicantForm(request.POST or None)
	if form.is_valid():

		name=form.cleaned_data['Your_name']
		idno=form.cleaned_data['Your_id']
		contact=form.cleaned_data['Your_contact']
		mail=form.cleaned_data['Your_email']
		amount=form.cleaned_data['Amount']
		date=form.cleaned_data['Date']
	
		
 
		p = applicant(Your_name=name, Your_id=idno, Your_contact=contact,
			Your_email=mail, Amount=amount, Date=date)
		p.save()
		return render(request, 'messages.html', {"title": "Loan"})


	context = {
	"form": form,
	}	
	
	return render(request, 'loan.html', context)



def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

def messages(request):
	return render(request, 'messages.html')

def approvedLoans(request):
	title = 'All Loans'
	queryset = applicant.objects.all()

	context = {
	"title": title,
	"querset": queryset,
	}
	return render(request, 'approved_loans.html', context)


def search(request):
	title="Search Applicant"
	form = AForm(request.POST or None)
	if form.is_valid():
		name = form.cleaned_data['Your_name']
		queryset= applicant.objects.filter(Your_name=name)
		context = {
		"title": title,
		"queryset": queryset,
		}
		return render(request, 'approved_loans.html', context)


	context = { 
	"title": title,
	"form": form
	}
	return render(request, 'search.html', context)

def loanApplicants(request):
	return render(request, 'loanApplicants.html')




