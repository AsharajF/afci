# Generated by Django 4.0.1 on 2022-06-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_cart_fees'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='link',
            field=models.URLField(null=True),
        ),
    ]
