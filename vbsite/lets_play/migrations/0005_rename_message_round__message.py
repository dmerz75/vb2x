# Generated by Django 4.2.4 on 2023-08-26 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lets_play', '0004_round_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='round',
            old_name='message',
            new_name='_message',
        ),
    ]