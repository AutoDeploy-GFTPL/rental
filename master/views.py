from django.shortcuts import render
from . models import *
from about . models import *
from blog . models import *
import random
from django.core.paginator import Paginator


def getGlobalContext(request):
    context = {}
    context['contact_heading'] = Headings.objects.filter(heading_type = 'Contact').last()
    context['about_heading'] = Headings.objects.filter(heading_type = 'About').last()
    context['propertyy_page'] = Property.objects.all()

    context['fb'] = SocialMedia.objects.filter(social_media = 'Facebook').last()
    context['ig'] = SocialMedia.objects.filter(social_media = 'Instagram').last()
    context['li'] = SocialMedia.objects.filter(social_media = 'Linkedin').last()
    context['tw'] = SocialMedia.objects.filter(social_media = 'Twitter').last()
    context['ytube'] = SocialMedia.objects.filter(social_media = 'Youtube').last()
    context['telg'] = SocialMedia.objects.filter(social_media = 'Telegram').last()
    context['whatsapp'] = SocialMedia.objects.filter(social_media = 'Whatsapp').last()
    context['threads'] = SocialMedia.objects.filter(social_media = 'Threads').last()

    context['section_logo'] = Section.objects.filter(section_type = 'Logo').last()
    context['company'] = Company.objects.all().last()

    # Property
    context['all_property'] = Property.objects.all().order_by('-id')
    context['property_section'] = Section.objects.filter(section_type = 'Property').last()

    # Category
    context['category'] = Category.objects.all().order_by('-id')

    # Blogs
    context['blogs'] = Blog.objects.all().order_by('-id')
    context['blogs_section_nav'] = Section.objects.filter(section_type = 'Blogs').last()

    # Testimonials
    context['testimonial'] = Testimonials.objects.all().order_by('-id') 
    context['testimonial_section'] = Section.objects.filter(section_type = 'Testimonials').last()

    # Gallery
    context['gallery'] = Gallery.objects.all().order_by('-id') 
    context['gallery_section'] = Section.objects.filter(section_type = 'Gallery').last()

    # About
    context['about'] = About.objects.all().last()
    context['about_section'] = Section.objects.filter(section_type = 'About').last()

    # We Provide
    context['we_provide'] = WeProvide.objects.all().order_by('-id')
    context['we_provide_section'] = Section.objects.filter(section_type = 'WeProvide').last()

    # About Home
    context['about_home'] = AboutHome.objects.all().order_by('-id')
    context['about_home_section'] = Section.objects.filter(section_type = 'AboutHome').last()

    # Numbers
    context['numbers'] = Numbers.objects.all()
    context['section_number'] = Section.objects.filter(section_type = 'Numbers').last()

    return context 

def PropertyPage(request):
    context = getGlobalContext(request)
    get_category = request.GET.get('category')
    sort_by = request.GET.get('sort_by')
    print(f"{sort_by = }")
    propertyy_page = Property.objects.all()
    property_page = Property.objects.all()
    if get_category:
        property_page = Property.objects.filter(category__slug = get_category).order_by('-id')

    if sort_by == "oldest":
        property_page = property_page.order_by('created_date') 
    elif sort_by == "newest":
        property_page = property_page.order_by('-created_date')  
    elif sort_by == "price_low":
        property_page = property_page.order_by('total')  
    elif sort_by == "price_high":
        property_page = property_page.order_by('-total')  
    else:
        property_page = property_page.order_by('-id')  

    location = request.GET.get('location', '')
    category = request.GET.get('category', '')
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 1000000)  # Default max price

    if location:
        property_page = property_page.filter(location__icontains=location)
    if category:
        property_page = property_page.filter(category__title__icontains=category)
    if min_price:
        property_page = property_page.filter(total__gte=min_price)
    if max_price:
        property_page = property_page.filter(total__lte=max_price)

    context['propertyy_page'] = propertyy_page
    context['all_property'] = property_page
    context['get_category'] = get_category
    context['sort_by'] = sort_by

    context['banner_nav'] =  'Apartments'
    context['banner'] = Banners.objects.filter(banner_type = 'Apartments').last()
    context['seo_apartment']     = SEO.objects.filter(page_type = 'Apartments').last()

    return render(request, "house_rent.html", context)

def apartmentDetailPage(request, slug=None):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['subject']
        message=request.POST['message']

        phone_pattern = r'^[0-9]{10}$'

        if not re.match(phone_pattern, phone):
            return JsonResponse({'success': False, 'message': 'Invalid phone number.<br>Please enter a valid 10-digit phone number.', 'color_class': 'error-toast'})
        
        new_email=ContactForm(email=email,name=name,message=message,phone=phone, subject=subject)

        try:
            new_email.save()
            email_password = Company.objects.all().last()
            if email_password:
                email_host_user = email_password.gmail_email
                email_host_password = email_password.password
                try:
                    email_thread = EmailThread(
                            subject='Enquiry Received',
                            message=f'Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}',
                            from_email=email_host_user,
                            recipient_list=[email_host_user],
                            auth_user=email_host_user,
                            auth_password=email_host_password
                        )
                    email_thread.start()
                except Exception as e:
                    print(e)
                    pass
            return JsonResponse({'success': True, 'message': 'Your request has been received!<br>We will get in touch with you shortly.', 'color_class' : 'success-toast'})
        except Exception as e:
            print(e)
            return JsonResponse({'success': False, 'message': str(e), 'color_class': 'error-toast'})
        
    context = getGlobalContext(request)
    get_apartment = Property.objects.filter(slug = slug).last()
    try:
        get_images = PropertyImage.objects.filter(property__id = get_apartment.id)
    except:
        get_images = []
    
    try: property = Property.objects.filter(category=get_apartment.category).order_by('-id')[:3]
    except: property = []

    context['get_apartment'] = get_apartment
    context['get_images'] = get_images
    context['property_releated'] = property

    context['banner_nav'] =  'Apartment Detail'
    context['banner'] = Banners.objects.filter(banner_type = 'Apartment Detail').last()

    return render(request, "apartment_detail.html", context)

def Homepage(request):
    context = getGlobalContext(request)
    context['homepage_banner'] = Banners.objects.filter(banner_type = 'HomePage').order_by('-id')
    context['for_rates_availability_headings'] = Headings.objects.filter(heading_type = 'For rates & Availability').last()
    context['apartment_headings'] = Headings.objects.filter(heading_type = 'Apartment').last()
    
    context['number_heading'] = Headings.objects.filter(heading_type = 'Numbers').last()
    context['gallery_heading'] = Headings.objects.filter(heading_type = 'Gallery').last()
    
    context['testimonials_heading'] = Headings.objects.filter(heading_type = 'Testimonials').last()
    context['blogs_heading'] = Headings.objects.filter(heading_type = 'Blogs').last()
    context['seo_index']     = SEO.objects.filter(page_type = 'Home').last()
    
    return render(request, "index.html", context)

def GalleryPage(request):
    context = getGlobalContext(request)
    context['banner_nav'] =  'Gallery'
    context['banner'] = Banners.objects.filter(banner_type = 'Gallery').last()
    context['seo_gallery']     = SEO.objects.filter(page_type = 'Gallery').last()

    return render(request, "gallery.html", context)

from django.http import JsonResponse
from django.core.mail import send_mail
import re
import threading

class EmailThread(threading.Thread):
    def __init__(self, subject, message, from_email, recipient_list, auth_user, auth_password):
        self.subject = subject
        self.message = message
        self.from_email = from_email
        self.recipient_list = recipient_list
        self.auth_user = auth_user
        self.auth_password = auth_password
        threading.Thread.__init__(self)

    def run(self):
        try:
            send_mail(
                self.subject,
                self.message,
                self.from_email,
                self.recipient_list,
                fail_silently=False,
                auth_user=self.auth_user,
                auth_password=self.auth_password,
            )
        except Exception as e:
            print(f"Email sending failed: {e}")

def ContactPage(request):
    context = getGlobalContext(request)
    if  request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['subject']
        message=request.POST['message']

        phone_pattern = r'^[0-9]{10}$'

        if not re.match(phone_pattern, phone):
            return JsonResponse({'success': False, 'message': 'Invalid phone number.<br>Please enter a valid 10-digit phone number.', 'color_class': 'error-toast'})
        
        new_email=ContactForm(email=email,name=name,message=message,phone=phone, subject=subject)
        new_email.save()

        try:
            email_password = Company.objects.all().last()
            if email_password:
                email_host_user = email_password.gmail_email
                email_host_password = email_password.password
                try:
                    email_password = Company.objects.all().last()
                    if email_password:
                        email_host_user = email_password.gmail_email
                        email_host_password = email_password.password

                        email_thread = EmailThread(
                            subject='Enquiry Received',
                            message=f'Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}',
                            from_email=email_host_user,
                            recipient_list=[email_host_user],
                            auth_user=email_host_user,
                            auth_password=email_host_password
                        )
                        email_thread.start()
                except Exception as e:
                    print(e)


            return JsonResponse({'success': True, 'message': 'Your request has been received!<br>We will get in touch with you shortly.', 'color_class' : 'success-toast'})
        except Exception as e:
            print(e)
            return JsonResponse({'success': False, 'message': str(e), 'color_class': 'error-toast'})
    context['banner_nav'] =  'Contact'
    context['banner'] = Banners.objects.filter(banner_type = 'Contact').last()
    context['seo_contact']     = SEO.objects.filter(page_type = 'Contact').last()

    return render(request, "contact.html", context)

def AboutPage(request):
    context = getGlobalContext(request)
    print(f"{context = }")
    context['banner_nav'] =  'About'
    context['banner'] = Banners.objects.filter(banner_type = 'About').last()
    context['seo_about']     = SEO.objects.filter(page_type = 'About').last()

    return render(request, "about.html", context)

def blogPage(request):
    context = getGlobalContext(request)
    cat_id  =   request.GET.get('cat_id')
    tags_id = request.GET.get('tags_id')
    print(cat_id)  
    if cat_id:
        blogs   = Blog.objects.filter(category__slug=cat_id).order_by('-id')
    elif tags_id:
        blogs   = Blog.objects.filter(tags__id=tags_id).order_by('-id')
    else:
        blogs = Blog.objects.all().order_by('-id')


    paginator   =   Paginator(blogs,10)
    page_number =   request.GET.get('page')
    page_obj    =   paginator.get_page(page_number)
    total_page  =   page_obj.paginator.num_pages
    context['cat_id']        = cat_id
    context['tags_id']       = tags_id
    context['blogs']         = page_obj
    context['blogss']         = Blog.objects.all()
    context['blogs_category']         = BlogCategory.objects.all()
    context['tags']         = Tags.objects.all()

    context['seo_blogs']     = SEO.objects.filter(page_type = 'Blogs').last()

    context['banner_nav'] =  'Blogs'
    context['banner'] = Banners.objects.filter(banner_type = 'Blogs').last()

    context['seo_blogs']     = SEO.objects.filter(page_type = 'Blogs').last()
    return render(request, "blogs.html", context)

def blogsDetail(request, slug=None):
    context = getGlobalContext(request)
    context['get_blog'] = Blog.objects.filter(slug=slug).last()
    context['banner_nav'] =  'Blog Detail'
    context['banner'] = Banners.objects.filter(banner_type = 'Blog Detail').last()

    return render(request, "blogs_detail.html", context)