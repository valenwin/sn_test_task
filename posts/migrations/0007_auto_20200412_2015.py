# Generated by Django 3.0.5 on 2020-04-12 20:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0006_remove_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like_voters',
            field=models.ManyToManyField(related_name='like_voters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='unlike_voters',
            field=models.ManyToManyField(related_name='unlike_voters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='LikeDislike',
        ),
    ]
