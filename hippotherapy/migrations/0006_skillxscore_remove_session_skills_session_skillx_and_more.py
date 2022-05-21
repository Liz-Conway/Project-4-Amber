# Generated by Django 4.0.3 on 2022-05-14 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hippotherapy', '0005_alter_session_skills_alter_session_tasks_skillscore'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillxScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='session',
            name='skills',
        ),
        migrations.AddField(
            model_name='session',
            name='skillx',
            field=models.ManyToManyField(related_name='skill_score', through='hippotherapy.SkillxScore', to='hippotherapy.skill'),
        ),
        migrations.AlterField(
            model_name='skillscore',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='score_session_old', to='hippotherapy.session'),
        ),
        migrations.AlterField(
            model_name='skillscore',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='score_skill_old', to='hippotherapy.skill'),
        ),
        migrations.AddField(
            model_name='skillxscore',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='score_session', to='hippotherapy.session'),
        ),
        migrations.AddField(
            model_name='skillxscore',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='score_skill', to='hippotherapy.skill'),
        ),
        migrations.AlterUniqueTogether(
            name='skillxscore',
            unique_together={('session', 'skill')},
        ),
    ]