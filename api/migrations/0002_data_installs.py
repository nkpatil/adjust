# Generated by Django 2.1.3 on 2020-03-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='installs',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
