# Generated by Django 4.2.11 on 2024-04-24 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_news_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='userId',
            field=models.IntegerField(default=0),
        ),
    ]
