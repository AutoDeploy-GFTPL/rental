from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


def rename_file(instance, filename):
    if filename.find('.') >= 0:
        dot_index = (len(filename) - filename.rfind('.', 1)) * (-1)
        filename = filename[0:dot_index]
    filename = '{}.{}'.format(filename, 'webp')
    return filename

class SocialMedia(models.Model):
    TypesOfSocialMedia = (('Facebook','Facebook'),('Instagram','Instagram'),('Linkedin','Linkedin'),
                            ('Twitter','Twitter'),('Youtube','Youtube'),('Telegram','Telegram'),
                            ('Whatsapp','Whatsapp'),('Threads','Threads'))
    social_media = models.CharField(max_length=100, choices=TypesOfSocialMedia, null=True)
    url = models.URLField(null=True)

    def __str__(self):
        return self.social_media

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=15)
    message = models.TextField()

class NewsLetter(models.Model):
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email
    
class Company(models.Model):
    company_name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    alternative_phone = models.CharField(max_length=15, null=True)
    google_map_url = models.CharField(max_length=1000, null=True, blank=True)
    favicon_icon=models.ImageField(upload_to=rename_file, null=True)
    logo_icon=models.ImageField(upload_to=rename_file, null=True)
    address = models.TextField(blank=True, null=True)
    footer_description = models.TextField(blank=True, null=True)
    footer_image = models.ImageField(upload_to=rename_file, null=True)
    country_code = models.CharField(max_length=10, null=True)
    gmail_email = models.EmailField(verbose_name='Email (Send Mail)', null=True, blank=True)
    password=models.CharField(max_length=350,verbose_name='Password (Send Mail)', blank=True)
    office_hours = models.CharField(max_length=150, null=True)

    def __str__(self) -> str:
        return f"company id-{self.id}"

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    
class Testimonials(models.Model):
    name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    review=models.TextField()
    # rating = models.FloatField(default=1)
    image = models.ImageField(upload_to=rename_file, null=True, blank=True)

    def __str__(self):
        return self.name

class SEO(models.Model):
    TypesOfPage = (('HomePage','HomePage'),('About','About'), ('Apartments','Apartments'),
                    ('Gallery','Gallery'), ('Blogs','Blogs'), ('Contact','Contact'),)
    page_type = models.CharField(max_length=200, choices=TypesOfPage, null=True)
    meta_title  = models.TextField(max_length=500,null=True, blank=True)
    meta_description  = models.TextField(max_length=500,null=True, blank=True)
    meta_keywords  = models.TextField(max_length=500,null=True, blank=True)
    canonical_tag  = models.TextField(max_length=500,null=True, blank=True)
    
    def __str__(self):
        return self.page_type

class Section(models.Model):
    TypesOfSection = (('Property','Property'),('Gallery','Gallery'),('About','About'), ('WeProvide','WeProvide'),
                      ('AboutHome','AboutHome'),('Numbers','Numbers'),
                      ('FAQ','FAQ'),('Blogs','Blogs'), ('Testimonials','Testimonials'),)
    section_type = models.CharField(max_length=150, choices=TypesOfSection, null=True)
    show = models.BooleanField(default=True)

class Banners(models.Model):
    types_banner_type = (('HomePage','HomePage'),('About','About'), ('Apartments','Apartments'), ('Apartment Detail','Apartment Detail'),
                         ('Gallery','Gallery'), ('Blogs','Blogs'), ('Blog Detail','Blog Detail'), ('Contact','Contact'),)
    banner_type = models.CharField(max_length=150, choices=types_banner_type)
    title = models.CharField(max_length=150)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to=rename_file, null=True)

    def __str__(self):
        return self.title

class Headings(models.Model):
    types_of_heading = (('For rates & Availability','For rates & Availability'), ('About','About'),('Apartment','Apartment'),
                        ('Numbers','Numbers'),('Gallery','Gallery'),('Contact','Contact'),('Testimonials','Testimonials'),('Numbers','Numbers'),
                        ('Blogs','Blogs'))
    heading_type = models.CharField(max_length=150, choices=types_of_heading)
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(null=True)

class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title

class Property(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    total = models.FloatField(default=0)
    bedroom = models.IntegerField(default=0)
    bathroom = models.IntegerField(default = 0)
    short_description = models.TextField(null=True)
    description = RichTextUploadingField()
    thumbnail_image = models.ImageField(upload_to=rename_file, null=True)
    slug = models.SlugField(unique=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    meta_title  = models.TextField(max_length=500,null=True, blank=True)
    meta_description  = models.TextField(max_length=500,null=True, blank=True)
    meta_keywords  = models.TextField(max_length=500,null=True, blank=True)
    canonical_tag  = models.TextField(max_length=500,null=True, blank=True)
    

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=rename_file)

    def __str__(self):
        return str(str(self.id) + ' ' + self.property.title + ' ' + str(self.image))

class Gallery(models.Model):
    image = models.ImageField(upload_to=rename_file)
    favourite = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class WeProvide(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=rename_file)

    def __str__(self):
        return self.title

class Numbers(models.Model):
    title = models.CharField(max_length=150)
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# class ApartmentBooking(models.Model):
#     name = models.CharField(max_length=255)
#     phone = models.CharField(max_length=20)
#     email = models.EmailField()
#     # family_member = models.PositiveIntegerField()
#     # children = models.PositiveIntegerField()
#     remarks = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.name} - {self.email}"
    