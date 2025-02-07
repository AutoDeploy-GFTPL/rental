from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



def rename_file(instance, filename):
    if filename.find('.') >= 0:
        dot_index = (len(filename) - filename.rfind('.', 1)) * (-1)
        filename = filename[0:dot_index]
    filename = '{}.{}'.format(filename, 'webp')
    return filename

class About(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)
    house_admin = models.ImageField(upload_to=rename_file)
    admin_name = models.CharField(max_length=150)
    admin_designation = models.CharField(max_length=150)
    admin_description = models.TextField(null=True)
    admin_signature = models.ImageField(upload_to=rename_file)
  
    def __str__(self):
        return self.title

class AboutHome(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextUploadingField(null=True)
    sequence = models.IntegerField(default=0)
    image = models.ImageField(upload_to=rename_file, null=True)

    def __str__(self):
        return self.title
