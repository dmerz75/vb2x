# Generated by Django 4.2.4 on 2023-08-23 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lets_play', '0002_alter_round_options_round_pubdate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='round',
            options={'ordering': ['-pub_date', '-num_players', 'non_exclusions']},
        ),
        migrations.RenameField(
            model_name='round',
            old_name='pubdate',
            new_name='pub_date',
        ),
    ]
