# Generated by Django 4.1.7 on 2023-04-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_category_all_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Рубрика', 'verbose_name_plural': 'Рубрики'},
        ),
        migrations.AlterField(
            model_name='category',
            name='input_text',
            field=models.CharField(help_text='Номер рубрики', max_length=200),
        ),
    ]