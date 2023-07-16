from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.

def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Gaven'
    feature1.details = 'I wanna get Supermans physique'
    feature1.is_true = True
    
    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Merwin'
    feature2.details = 'I wanna get Virat Kholis physique'
    feature2.is_true = True
    
    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Sahil'
    feature3.details = 'I love Calisthenics'
    feature3.is_true = False
    
    features = [feature1,feature2,feature3]
    
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
    words = request.POST['words']
    amount_of_words = len(words.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
