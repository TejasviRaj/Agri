# Generated by Django 2.0 on 2018-01-03 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0004_auto_20180103_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='soilfield',
            name='irrigation',
            field=models.CharField(default='Yes', max_length=200),
            preserve_default=False,
        ),
    ]