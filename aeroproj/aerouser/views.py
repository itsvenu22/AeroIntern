from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import userdata

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
    if request.method == 'POST':
        # Assuming you receive data through a POST request
        field1_data = request.POST.get('username')  
        field2_data = request.POST.get('email')   
        field3_data = request.POST.get('password')
        # Create an instance of YourModel
        new_entry = userdata(username=field1_data, email=field2_data,password=field3_data)

        # Save the data to the database
        new_entry.save()

        return HttpResponse("success")
    else:
        return render(request, "signup.html")

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
