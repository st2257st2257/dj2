# Generated by Django 4.2.11 on 2024-04-24 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_user_token_alter_user_userrole'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userRole',
        ),
    ]