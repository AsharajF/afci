# Generated by Django 4.0.1 on 2022-03-04 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('bimage', models.ImageField(upload_to='bracnchimg')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('fees', models.IntegerField()),
                ('cimage', models.ImageField(upload_to='courseimg')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('bran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.branch')),
            ],
        ),
    ]