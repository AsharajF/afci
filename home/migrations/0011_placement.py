# Generated by Django 4.0.1 on 2022-05-31 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_rename_course_timetable_c_ourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('number', models.IntegerField()),
                ('wnumber', models.IntegerField()),
                ('quali', models.CharField(blank=True, max_length=25)),
                ('work_ex', models.CharField(blank=True, max_length=25)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=10)),
                ('interest', models.CharField(max_length=50)),
            ],
        ),
    ]