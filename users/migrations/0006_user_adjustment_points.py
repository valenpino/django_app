# Generated by Django 3.0.7 on 2020-07-01 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_is_shadow_banned'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='adjustment_points',
            field=models.IntegerField(default=0),
        ),
    ]
