from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField(default=1)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date_updated',)