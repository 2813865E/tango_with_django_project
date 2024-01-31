from django.db import models

# Create your models here.
class Category(models.Model):
    #note unique means the name must be unique 
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

class Page(models.Model):
    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url = models.URLField()
    views = models.IntegerField(default=0)
    

    def __str__(self):
     return self.title