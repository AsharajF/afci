# Generated by Django 4.0.1 on 2022-05-20 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_courses_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='des',
            field=models.CharField(default=False, max_length=1500),
        ),
    ]
