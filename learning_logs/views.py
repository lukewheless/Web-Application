from django.shortcuts import render
from .models import Topic

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










