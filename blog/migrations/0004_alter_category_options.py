# Generated by Django 5.0.4 on 2024-04-25 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name_plural': 'categories'},
        ),
    ]