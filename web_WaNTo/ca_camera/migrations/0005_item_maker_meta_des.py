# Generated by Django 3.1.7 on 2021-03-23 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca_camera', '0004_auto_20210323_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_maker',
            name='meta_des',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
