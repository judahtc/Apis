# Generated by Django 3.2.7 on 2022-03-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_universities'),
    ]

    operations = [
        migrations.AddField(
            model_name='universities',
            name='programme_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='universities',
            name='programme_name',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
