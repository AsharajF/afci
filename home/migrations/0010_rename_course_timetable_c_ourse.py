# Generated by Django 4.0.1 on 2022-05-28 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_offers_timetable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetable',
            old_name='course',
            new_name='c_ourse',
        ),
    ]
