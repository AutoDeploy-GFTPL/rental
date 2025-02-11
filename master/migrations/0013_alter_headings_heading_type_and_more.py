# Generated by Django 4.2.18 on 2025-02-05 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0012_numbers_alter_headings_heading_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headings',
            name='heading_type',
            field=models.CharField(choices=[('For rates & Availability', 'For rates & Availability'), ('About', 'About'), ('Apartment', 'Apartment'), ('Numbers', 'Numbers'), ('Contact', 'Contact'), ('Testimonials', 'Testimonials'), ('Numbers', 'Numbers')], max_length=150),
        ),
        migrations.AlterField(
            model_name='section',
            name='section_type',
            field=models.CharField(choices=[('Property', 'Property'), ('Gallery', 'Gallery'), ('About', 'About'), ('WeProvide', 'WeProvide'), ('AboutHome', 'AboutHome'), ('Numbers', 'Numbers'), ('FAQ', 'FAQ'), ('Blogs', 'Blogs'), ('Testimonials', 'Testimonials')], max_length=150, null=True),
        ),
    ]
