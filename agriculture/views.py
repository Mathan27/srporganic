from django.shortcuts import render,redirect
from .models import register,adminpanel,adminfruits,adminveg,admintubers,admingreens
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def nav(request,id):
    output = register.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        register.objects.filter(id=id).update(name=name,email=email,phone=phone)
        User.objects.filter(id=id).update(username=name,email=email)
        return redirect('home')
        # return render(request,'update.html',{'output': output})
    return render(request,'update.html',{'output':output})


def profile(request):
    return render(request,'profile.html')

def home(request):
    return render(request,'home.html')

def dashboard(request):
    contents = adminpanel.objects.all()
    return render(request,'dashboard.html',{'contents':contents})

def fruits(request):
    contents = adminfruits.objects.all()
    return render(request,'fruits.html',{'contents':contents})

def vegs(request):
    contents = adminveg.objects.all()
    return render(request,'vegs.html',{'contents':contents})

def tubers(request):
    contents = admintubers.objects.all()
    return render(request,'tubers.html',{'contents':contents})

def greens(request):
    contents = admingreens.objects.all()
    return render(request,'greens.html',{'contents':contents})

def logininfo(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        if name and password:
            user = auth.authenticate(username = name , password = password)
            if user is not None:
                auth.login(request,user)
                messages.info(request,"Login Successfully")
                return redirect("/")
            else:
                messages.info(request,"Invalid Data")
                return redirect('login')
    else:
        return render(request,'login.html')

def registeration(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.info(request,'Email exists')
            return redirect('register')
        elif User.objects.filter(username=name).exists():
            messages.info(request,'Name exists')
            return redirect('register')
        else:
            data = register(name=name,phone=phone,email=email,password=password)
            data.save()
            user = User.objects.create_user(username=name,password=password,email=email)
            user.save()
            return redirect('/login')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def viewdetail(request,name):
    if(name == 'CROP Cultivation'):
        return render(request,'crop.html')
    elif(name == 'FRUITS Cultivation'):
        return redirect('fruits')
    elif(name == 'TUBER Cultivation'):
        return redirect('tubers')
    elif(name == 'VEGETABLE Cultivation'):
        return redirect('vegs')
    elif(name == 'GREENS Cultivation'):
        return redirect('greens')

def viewfruits(request,name):
    if(name == 'MANGO Cultivation'):
        return render(request,'mango.html')
    elif(name == 'GUAVA Cultivation'):
        return render(request,'guva.html')
    else:
        return render(request,'pome.html')

def viewtubers(request, name):
    if(name == 'BEETROOT Cultivation'):
        return render(request,'betroot.html')
    elif(name == 'POTATO Cultivation'):
        return render(request,'potato.html')
    else:
        return render(request,'carroot.html')

def viewvegs(request,name):
    if(name == 'TOMATO Cultivation'):
        return render(request,'tomato.html')       
    elif(name == 'CABBAGE Cultivation'):
        return render(request,'cabbage.html')
    elif(name == 'CUCUMBER Cultivation'):
        return render(request,'cucumber.html')

def viewgreens(request,name):
    if(name == 'CURRY Cultivation'):
        return render(request,'curry.html')
    elif(name == 'CORIANDER Cultivation'):
        return render(request,'Coriander.html')
    elif(name == 'LETTUCE Cultivation'):
        return render(request,'lettuce.html')
            
def profile(request,id):
    output = register.objects.all()
    return render(request,'')