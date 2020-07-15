from django.shortcuts import render
from .models import Destination2
# Create your views here.


def intern(request):
    return render(request, 'intern.html')

def newPage(request):
    if request.method=="POST":
        First_name=request.POST['First_name']
        Middle_name=request.POST['Middle_name']
        Last_name=request.POST['Last_name']
        Company_name=request.POST['Company_name']
        Mobile_Number=request.POST['Mobile_Number']
        Email=request.POST['Email']
        Date_of_Birth=request.POST['Date_of_Birth']
        Pin_Code=request.POST['Pin_Code']
        District=request.POST['District']
        State=request.POST['State']
        City=request.POST['City']
        Address=request.POST['Address']
        Adhaar_Card=request.POST.get('Adhaar_Card')
        Pan_Card=request.POST.get('Pan_Card')

        ins= Destination2(First_name=First_name,Middle_name=Middle_name,Last_name=Last_name,Company_name=Company_name,Mobile_Number=Mobile_Number,Email=Email,Date_of_Birth=Date_of_Birth,Pin_Code=Pin_Code,District=District,State=State,City=City,Address=Address,Adhaar_Card=Adhaar_Card,Pan_Card=Pan_Card)
        ins.save()
    return None

