# Generated by Django 5.0.4 on 2024-05-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='img',
            field=models.ImageField(default='Images/None/Noimg.jpg', upload_to='Images/'),
        ),
    ]
