# Generated by Django 4.0.3 on 2022-05-17 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hippotherapy', '0008_alter_skillscore_session_alter_skillscore_skill_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='skillx',
        ),
        migrations.DeleteModel(
            name='SkillxScore',
        ),
    ]
