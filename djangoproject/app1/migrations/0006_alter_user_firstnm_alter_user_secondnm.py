# Generated by Django 4.2.11 on 2024-04-24 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_user_userrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='firstNM',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='secondNM',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]