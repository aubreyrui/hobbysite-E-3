# Generated by Django 5.0.3 on 2024-03-19 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commission',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commission',
            name='people_required',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
