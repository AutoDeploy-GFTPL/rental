from django.contrib import admin
from . models import *


admin.site.register(NewsLetter)
admin.site.register(Testimonials)

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone','subject']
    list_display_links = ['name', 'email', 'phone','subject']
    
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'email', 'phone']
    list_display_links = ['id', 'email', 'phone']

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'section_type', 'show']
    list_display_links = ['id', 'section_type', 'show']
    
@admin.register(FAQ)
class FAQDisplay(admin.ModelAdmin):
    list_display = ('id', )
    
@admin.register(Headings)
class HeadingsDisplay(admin.ModelAdmin):
    list_display = ('id', 'heading_type', 'title', 'description')
    
@admin.register(Banners)
class HeadingsAndBannersDisplay(admin.ModelAdmin):
    list_display = ('id', 'banner_type', 'title', 'description')
    
@admin.register(SEO)
class SEODisplay(admin.ModelAdmin):
    list_display = ('id', 'page_type')
    
class PropertyImageInline(admin.TabularInline):  # Alternatively, use StackedInline
    model = PropertyImage
    extra = 1  # Extra blank forms for adding new images

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'total', 'bedroom', 'bathroom')
    search_fields = ('title', 'category__title', 'location')
    list_filter = ('category', 'location')
    inlines = [PropertyImageInline]  # Inline images inside Property

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'image')

admin.site.register(SocialMedia)
admin.site.register(Gallery)
admin.site.register(WeProvide)
admin.site.register(Numbers)

