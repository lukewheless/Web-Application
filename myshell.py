import os 
import django 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")
django.setup()

from learning_log.models import Topic

topics = Topic.objects.all()

for topic in topic:
    print("Topic ID:", topic.id, " Topic:", topic)

t = Topic.objects.get(id=1)
print(t.text)
print(t.date_added)

entries = t.entry_set.all()

for entry in entries:
    print(entry)









