# Generated by Django 2.0 on 2018-01-03 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0005_soilfield_irrigation'),
    ]

    operations = [
        migrations.AddField(
            model_name='soilfield',
            name='type',
            field=models.CharField(default='Food Crop', max_length=200),
            preserve_default=False,
        ),
    ]
