# Generated by Django 2.0.2 on 2018-04-04 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_auto_20180404_1227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'get_latest_by': 'asked', 'ordering': ('asked',)},
        ),
    ]
