# Generated by Django 3.1.7 on 2021-02-25 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_wantoitem_maker_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wantoitem',
            name='maker_slug',
        ),
        migrations.AddField(
            model_name='item_maker',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]