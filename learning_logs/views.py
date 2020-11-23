from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

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
    entries = topic.entry_set.order_by("-date_added") # desc order (-)

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

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = TopicForm() #blank form
    else:
        form = EntryForm(data=request.POST) #all info from user onto form

        if form.is_valid():
            new_entry = form.save(commit=False)     #saves form directly to topic model

            new_entry.topic = topic
            new_entry.save()
            form.save()
            return redirect('learning_logs:topic',topic_id=topic_id)
    
    context = {'form':form, 'topic':topic}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = Entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry) # loads form with existing entry 
    else:
        form = EntryForm(instance=entry, data=request.POST) 

        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', t_id=topic.id) 
    
    context = {'entry':entry, 'topic':topic, 'form':form} #function of context that shows us a view of data we want to see
    return render(request, 'learning_logs/edit_entry.html', context)