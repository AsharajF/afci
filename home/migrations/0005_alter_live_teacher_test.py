# Generated by Django 4.0.1 on 2022-05-19 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_live_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='live',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Topic', models.CharField(max_length=50)),
                ('scheduled', models.DateTimeField(auto_now_add=True, null=True)),
                ('link', models.URLField(null=True)),
                ('c_ourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.courses')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
