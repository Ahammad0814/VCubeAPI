# Generated by Django 5.0.2 on 2024-06-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student_Files_Data',
        ),
        migrations.AddField(
            model_name='studentdata',
            name='Image',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='Resume',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
