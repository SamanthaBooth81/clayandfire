# Generated by Django 3.2 on 2022-05-26 08:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_ratingreview'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RatingReview',
            new_name='Review',
        ),
    ]
