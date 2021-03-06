# Generated by Django 3.1.7 on 2021-03-06 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item_maker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Wantoitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('maker_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wantem.item_maker')),
                ('tag', models.ManyToManyField(blank=True, to='wantem.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_url', models.URLField()),
                ('sub_title', models.CharField(max_length=255)),
                ('sub_ogp_img', models.URLField(blank=True, null=True)),
                ('wantoitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wantem.wantoitem')),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_url', models.URLField()),
                ('main_title', models.CharField(max_length=255)),
                ('main_ogp_img', models.URLField(blank=True, null=True)),
                ('wantoitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wantem.wantoitem')),
            ],
        ),
    ]
