# Generated by Django 3.2.8 on 2021-11-12 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
