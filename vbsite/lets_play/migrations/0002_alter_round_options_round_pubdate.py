# Generated by Django 4.2.4 on 2023-08-23 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lets_play', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='round',
            options={'ordering': ['-pubdate', '-num_players', 'non_exclusions']},
        ),
        migrations.AddField(
            model_name='round',
            name='pubdate',
            field=models.DateField(default=None, help_text='Round publish date.', null=True),
        ),
    ]