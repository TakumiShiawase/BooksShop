# Generated by Django 4.2.1 on 2023-05-25 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='coverpage',
            field=models.ImageField(default='default_book_img.png', upload_to='book_images'),
        ),
    ]
