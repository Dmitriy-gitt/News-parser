# Generated by Django 4.1.7 on 2023-04-04 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='all_category',
            field=models.TextField(null=True),
        ),
    ]
