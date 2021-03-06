# Generated by Django 3.2 on 2021-04-14 00:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210409_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='juki',
            name='atteint',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='juki',
            name='objectifLecture',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='juki',
            name='chosedBy',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='juki',
            name='fromRecital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.recital'),
        ),
    ]
