# Generated by Django 2.2.8 on 2020-03-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20200326_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherdata',
            name='nengetu',
            field=models.CharField(default=202001, max_length=6, verbose_name='年月'),
        ),
    ]
