from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required 
from django.http import Http404

# Create your views here.
def index(request):
    return render(request,'learning_logs/index.html')

#to get all topics
@login_required             #processes this instruction before access info
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    #specific filter for users topics

    context = {'topics': topics}

    return render(request,'learning_logs/topics.html', context)

#individual topics
@login_required 
def topic(request, t_id):
    topic = Topic.objects.get(id=topic_id)

    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by("-date_added") # desc order (-)
    
    context = {'topic': topic, 'entries': entries}

    return render(request,'learning_logs/topic.html', context)

#get read data from database
#post sends data to database
@login_required 
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm() #blank form
    else:
        form = TopicForm(data=request.POST) #all info from user onto form

        if form.is_valid():
            new_topic = form.save(commit=False)     #saves form directly to topic model
            new_topic.owner = request.user
            new_topic.save()

            return redirect('learning_logs:topics')
    
    context = {'form':form}

    return render(request, 'learning_logs/new_topic.html', context)

@login_required 
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

@login_required 
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry) # loads form with existing entry 
    else:
        form = EntryForm(instance=entry, data=request.POST) 

        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', t_id=topic.id) 
    
    context = {'entry':entry, 'topic':topic, 'form':form} #function of context that shows us a view of data we want to see
    return render(request, 'learning_logs/edit_entry.html', context)