# Generated by Django 4.0.1 on 2022-05-20 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_live_teacher_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='des',
            field=models.CharField(default=True, max_length=1500),
        ),
    ]
