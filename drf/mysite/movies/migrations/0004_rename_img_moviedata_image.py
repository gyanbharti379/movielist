# Generated by Django 5.0.4 on 2024-05-22 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_moviedata_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviedata',
            old_name='img',
            new_name='image',
        ),
    ]