# Generated by Django 2.0.1 on 2018-01-19 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20180117_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='num_comments',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
