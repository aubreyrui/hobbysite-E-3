# Generated by Django 5.0.3 on 2024-03-16 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'ordering': ['name'], 'verbose_name': 'article category', 'verbose_name_plural': 'article categories'},
        ),
    ]
