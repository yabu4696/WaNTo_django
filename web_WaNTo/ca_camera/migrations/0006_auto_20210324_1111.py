# Generated by Django 3.1.7 on 2021-03-24 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca_camera', '0005_item_maker_meta_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_maker',
            name='meta_des',
            field=models.CharField(default='<meta name="description" content="カメラのレビューや評価サイトだけを表示したいというお悩みはありませんか？本サイトでは、カメラのレビューや評価サイトサイトだけを一覧表示！あなたに最適なアイテムを見つけてください。">', max_length=255),
        ),
        migrations.AlterField(
            model_name='wantoitem',
            name='meta_des',
            field=models.CharField(default='<meta name="description" content="カメラのレビューや評価サイトだけを表示したいというお悩みはありませんか？本サイトでは、カメラのレビューや評価サイトサイトだけを一覧表示！あなたに最適なアイテムを見つけてください。">', max_length=255),
        ),
    ]