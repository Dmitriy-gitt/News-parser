# Generated by Django 4.1.7 on 2023-04-09 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='all_topic',
            new_name='name_topic',
        ),
    ]