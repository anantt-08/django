from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, "index.html")

def adminlogin(request):
	return render(request, "AdminLogin.html",{'msg':""})

def userlogin(request):
	return render(request, "UserLogin.html",{'msg':""})
				