# Generated by Django 4.2.4 on 2023-09-27 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_catagory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='catagory',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.TextField(),
        ),
    ]
