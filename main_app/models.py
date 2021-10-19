from django.db import models

# Create your models here.

class Army(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    desc = models.TextField(max_length=1000)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Mini(models.Model):

    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    army = models.ForeignKey(Army, on_delete=models.CASCADE, related_name='Miniatures')

    def __str__(self):
        return self.title
