from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)

class Meditation(models.Model):
    meditation = models.ForeignKey(User, on_delete=models.CASCADE)
    meditation_type = models.CharField(max_length=30)
    duration = models.TimeField(auto_now=False, auto_now_add=False)
    pub_date = models.DateTimeField('meditation date')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
