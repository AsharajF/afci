# Generated by Django 4.0.1 on 2022-06-02 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_rename_fees_courses_fees1_courses_fees2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='fees1',
            new_name='fees',
        ),
    ]