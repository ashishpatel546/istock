# Generated by Django 3.2.4 on 2021-11-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preipo', '0002_auto_20211107_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='preipo',
            name='url',
            field=models.CharField(default='abc', max_length=100),
            preserve_default=False,
        ),
    ]