# Generated by Django 3.2 on 2021-04-09 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recital',
            name='recitalType',
            field=models.TextField(choices=[('PUBLIC', 'PUBLIC'), ('PRIVATE', 'PRIVATE')], default='PUBLIC', max_length=90),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='juki',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='kamil',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='like',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
