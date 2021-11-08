# Generated by Django 3.2.4 on 2021-11-07 11:54

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('preipo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preipo',
            name='Script_pic',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='IPO/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='preipo',
            name='Desc',
            field=tinymce.models.HTMLField(),
        ),
    ]
