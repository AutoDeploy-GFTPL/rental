from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

def rename_file(instance, filename):
    if filename.find('.') >= 0:
        dot_index = (len(filename) - filename.rfind('.', 1)) * (-1)
        filename = filename[0:dot_index]
    filename = '{}.{}'.format(filename, 'webp')
    return filename

#---------------BLOGS---------------
class BlogCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name
    
class Tags(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Tags'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name

class Blog(models.Model):
    category    = models.ForeignKey(BlogCategory,on_delete=models.CASCADE,null=True, blank=True)
    title       = models.CharField(max_length=250)
    author       = models.CharField(max_length=250)
    short_description = models.TextField(null=True)
    description = RichTextUploadingField(null=True)
    image       = models.ImageField(null=True,blank=True)
    date        = models.DateField(auto_now_add=True)
    tags        = models.ManyToManyField(Tags, blank=True)
    slug        = models.SlugField(unique=True, blank=True)
    meta_title  = models.TextField(max_length=500,null=True, blank=True)
    meta_description  = models.TextField(max_length=500,null=True, blank=True)
    meta_keywords  = models.TextField(max_length=500,null=True, blank=True)
    canonical_tag  = models.TextField(max_length=500,null=True, blank=True)

    def __str__(self):
        return self.title
