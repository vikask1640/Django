from django.shortcuts import render

def index(request):
	return render(request,'personal/home.html')
	
def contact(request):
	return render(request,'personal/contacts.html',{'content':['If you like to contact me please email me','vikas84r@gmail.com']})
