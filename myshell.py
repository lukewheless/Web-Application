import os 
import django
from learning_log.models import Topic
from django.contrib.auth.models import User 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")
django.setup()

topics = Topic.objects.all()

for topic in topic:
    print("Topic ID:", topic.id, " Topic:", topic)

t = Topic.objects.get(id=1)
print(t.text)
print(t.date_added)

entries = t.entry_set.all()

for entry in entries:
    print(entry)

for user in User.objects.all():
    print(user.username, user.id)









