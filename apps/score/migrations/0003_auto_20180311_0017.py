# Generated by Django 2.0.2 on 2018-03-11 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0002_auto_20180311_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answersheet',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire_level_answerSheet', to='score.Questionnaire', verbose_name='对应问卷'),
        ),
    ]