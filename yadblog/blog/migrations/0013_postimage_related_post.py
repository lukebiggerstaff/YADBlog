# Generated by Django 2.0.1 on 2018-01-12 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180110_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimage',
            name='related_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
