# Generated by Django 3.2.2 on 2022-10-27 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_auto_20221026_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialpost',
            name='shared_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
