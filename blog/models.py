from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
import time
from random import choice
from os.path import join as path_join
from os import listdir
from os.path import isfile
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, help_text="The link your post will be live at. Must be unique.")
    updated_on = models.DateTimeField(auto_now= True)
    content = HTMLField('Content')
    # def random_img():
    #     dir_path = 'static/blog/thumbnails'
    #     files = [content for content in listdir(dir_path) if isfile(path_join(dir_path, content))]
    #     return path_join(dir_path, choice(files))
    # def get_absolute_url(self):
    #     return "/" + self.slug
    # image = models.ImageField(default=random_img, blank=True, upload_to='static/blog/images', help_text="TRY TO KEEP THIS IMAGE UNDER 500KB. This will be the image that appears with the blog post on the home page")
    # hero_image = models.BooleanField(default=False, help_text="Checking this will display the fullscreen image on the post page.", verbose_name="Full Screen Image")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    embed = models.TextField(null=True, blank=True, help_text="Paste an embed link here and it will show up at the bottom of the post.")


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Flatpage(models.Model):
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title

