# Generated by Django 3.1.7 on 2021-03-23 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca_camera', '0003_auto_20210323_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wantoitem',
            name='meta_des',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]