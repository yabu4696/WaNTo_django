# Generated by Django 3.1.7 on 2021-03-24 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca_camera', '0006_auto_20210324_1111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item_maker',
            options={'ordering': ['the_order']},
        ),
        migrations.AddField(
            model_name='item_maker',
            name='the_order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
    ]