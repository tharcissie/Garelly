# Generated by Django 3.1.4 on 2020-12-19 16:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0003_auto_20201219_1216'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='image',
            name='author',
            field=models.CharField(default='admin', max_length=40),
        ),
        migrations.AddField(
            model_name='image',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
