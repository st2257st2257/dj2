# Generated by Django 4.2.11 on 2024-04-24 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_rename_massage_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='firstUserId',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='secondUserId',
        ),
        migrations.RemoveField(
            model_name='message',
            name='chatId',
        ),
        migrations.RemoveField(
            model_name='message',
            name='userId',
        ),
        migrations.AddField(
            model_name='chat',
            name='chatTitle',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='chat',
            name='firstUserLogin',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='chat',
            name='secondUserLogin',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='message',
            name='chatName',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='message',
            name='userLogin',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
