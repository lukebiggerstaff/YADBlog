# Generated by Django 2.0.1 on 2018-01-11 00:32

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180110_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/blog/media'), upload_to=''),
        ),
    ]
