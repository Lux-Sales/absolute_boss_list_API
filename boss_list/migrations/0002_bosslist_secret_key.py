# Generated by Django 3.1.6 on 2021-02-21 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bosslist',
            name='secret_key',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
