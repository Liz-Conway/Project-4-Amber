# Generated by Django 4.0.3 on 2022-06-14 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hippotherapyuser',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Administrator'), (2, 'Occupational Therapist'), (3, 'Hippotherapy Analyst')], null=True),
        ),
    ]
