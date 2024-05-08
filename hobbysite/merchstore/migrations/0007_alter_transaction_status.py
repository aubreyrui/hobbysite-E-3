# Generated by Django 5.0.2 on 2024-05-08 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0006_alter_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('On Cart', 'On Cart'), ('To Pay', 'To Pay'), ('To Ship', 'To Ship'), ('To Receive', 'To Receive'), ('Delivered', 'Delivered')], max_length=64),
        ),
    ]
