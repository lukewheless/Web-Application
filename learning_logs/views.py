from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

# Create your views here.
def index(request):
    return render(request,'learning_logs/index.html')

#to get all topics
def topics(request):
    topics = Topic.objects.order_by("date_added")

    context = {'topics': topics}

    return render(request,'learning_logs/topics.html', context)

#individual topics
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.rder_by("-date_added") # desc order (-)

    context = {'topic': topic, 'entries': entries}

    return render(request,'learning_logs/topic.html', context)


#get read data from database
#post sends data to database

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm() #blank form
    else:
        form = TopicForm(data=request.POST) #all info from user onto form

        if form.is_valid():
            form.save()     #saves form directly to topic model

            return redirect('learning_logs:topics')
    
    context = {'form':form}

    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = TopicForm() #blank form
    else:
        form = TopicForm(data=request.POST) #all info from user onto form

        if form.is_valid():
            new_entry = form.save()     #saves form directly to topic model

            new_entry.topic = topic
            new_entry.save()
            form.save()
            return redirect('learning_logs:topics',topic_id=topic_id)
    
    context = {'form':form, 'topic':topic}

    return render(request, 'learning_logs/new_topic.html', context)












