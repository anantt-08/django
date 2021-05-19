from django.shortcuts import render

# Create your views here.

def checkadminlogin(request):
	userid=str(request.POST['adminid'])
	password=str(request.POST['password'])
	if( userid == "admin" and password == "1234"):
		mssg = userid
	else:
		mssg  = userid
	return render(request, "admin_dashboard.html",{'msg':mssg})
		