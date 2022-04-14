# Generated by Django 2.2 on 2022-04-06 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('is_bestselling', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
    ]
