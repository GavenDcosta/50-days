from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages

#from .models import Feature

# Create your views here.

def index(request):
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Gaven'
    # feature1.details = 'I wanna get Supermans physique'
    # feature1.is_true = True
    
    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Merwin'
    # feature2.details = 'I wanna get Virat Kholis physique'
    # feature2.is_true = True
    
    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = 'Sahil'
    # feature3.details = 'I love Calisthenics'
    # feature3.is_true = False
    
    # features = [feature1,feature2,feature3]
    
    
    features = Attribute.objects.all()
    
    context = {
        'name' : 'Gaven',
        'age' : 20,
        'nationality' : 'Indian',
        'features' : features
        # 'feature1' : feature1,
        # 'feature2' : feature2,  
        # 'feature3' : feature3      
    }
    return render(request, 'index.html', context)
    

def counter(request): 
    # words = request.GET['words']  #name of the text area....put the url name in action attribute
    #POST is more secure than GET because in GET all the data gets visible on the url..but in POST its hidden
    
    # words = request.POST['words']
    # amount_of_words = len(words.split())
    # return render(request, 'counter.html', {'amount': amount_of_words})
    
    posts = [1,2,3,4,5,'tim','tom','john']
    return render(request, 'counter.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already in Use')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Successfully Registered')
                return redirect('login')
        else:
            messages.error(request, 'Passwords Do Not Match')  
            return redirect('register')
           
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Credentials Invalid')  
            return redirect('login') 
        
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/') 


#dynamic routing
def post(request, pk):
    return render(request, 'post.html',{'pk':pk})
    
