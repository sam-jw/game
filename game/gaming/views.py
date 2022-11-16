from django.shortcuts import render

# Create your views here.
def game(request):
    return render(request,'index.html')

def startgame(request):
    return render(request,'startgame.html')

def levelgame(request):
    return render(request,'levelgame.html')

def category(request):
    return render(request,'home.html')
