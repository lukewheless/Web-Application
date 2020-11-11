from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'learning_logs/index.html')

def topics(request):
    return render(request,'learning_logs/topic.html')









