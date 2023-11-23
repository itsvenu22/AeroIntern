from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import userdata
from django.contrib.auth.hashers import make_password

def login(request):
    #template = userdata.objects.all().values()
    template = loader.get_template('login.html')
    context = {
    'udatas': template,
    }
    return HttpResponse(template.render(context, request))
'''
def signup(request):
    print(request.GET)
    return render(request, "signup.html")'''

def signup(request):
    error_message = None 
    if request.method == 'POST':
        # Assuming you receive data through a POST request
        field1_data = request.POST.get('username')  
        field2_data = request.POST.get('email')   
        field3_data = request.POST.get('password')
        # Create an instance of YourModel
       
        if userdata.objects.filter(email=field2_data).exists():
            error_message = "Email already exists in the database."
            return render(request, "signup.html", {'error_message': error_message})
        else:
            hashed_password = make_password(field3_data)
            new_entry = userdata(username=field1_data, email=field2_data, password=hashed_password)
            new_entry.save()
            return HttpResponse("Signup successful")
    else:
        return render(request, "signup.html", {'error_message': error_message}) 

      

'''
def details(request,id):
    myuser = userdata.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
    'udata': myuser,
    }
    return HttpResponse(template.render(context, request))
'''
# Create your views here.
