# Generated by Django 4.0.3 on 2022-05-21 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0006_alter_task_task_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='diagnosis',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
