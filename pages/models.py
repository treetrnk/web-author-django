from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(null=True, populate_from='title')
    parent = models.ForeignKey('self', on_delete=models.PROTECT, blank=True)
    banner = models.CharField(max_length=1000, blank=True)
    tags = models.CharField(max_length=1000, blank=True)
    sidebar = models.TextField(blank=True)
    body = models.TextField()    
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.title

    def save_model(self, request, obj, form, change):
        """When creating a new object, set the creator field.
        """
        if not change:
            obj.author = request.user
        obj.save()