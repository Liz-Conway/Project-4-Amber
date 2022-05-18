# Generated by Django 4.0.3 on 2022-05-14 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hippotherapy', '0007_session_skill_alter_session_skillx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillscore',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='score_session', to='hippotherapy.session'),
        ),
        migrations.AlterField(
            model_name='skillscore',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='score_skill', to='hippotherapy.skill'),
        ),
        migrations.AlterField(
            model_name='skillxscore',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='score_x_session', to='hippotherapy.session'),
        ),
        migrations.AlterField(
            model_name='skillxscore',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='score_x_skill', to='hippotherapy.skill'),
        ),
    ]
