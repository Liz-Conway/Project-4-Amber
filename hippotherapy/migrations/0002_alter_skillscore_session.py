# Generated by Django 4.0.3 on 2022-06-26 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hippotherapy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillscore',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_session', to='hippotherapy.session'),
        ),
    ]
