# Generated by Django 4.0.3 on 2022-04-30 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_friend_alter_diagnosis_diagnosis'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
