# Generated by Django 4.2.18 on 2025-02-03 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_alter_section_section_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
