# Generated by Django 5.0.2 on 2024-06-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0004_studentdata_github_studentdata_linkedin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='Github',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Linkedin',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
