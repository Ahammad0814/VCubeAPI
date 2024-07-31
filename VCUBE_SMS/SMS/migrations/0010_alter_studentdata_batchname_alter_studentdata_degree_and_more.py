# Generated by Django 5.0.2 on 2024-06-28 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0009_studentdata_authentication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='BatchName',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Degree',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Degree_Branch',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Degree_CGPA',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Degree_Year',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Inter',
            field=models.CharField(default='12th', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Inter_Branch',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Inter_CGPA',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Inter_Year',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='JoiningDate',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='PG',
            field=models.CharField(default='N/A', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='PG_Branch',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='PG_CGPA',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='PG_Year',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Phone',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='SSC',
            field=models.CharField(default='10th', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='SSC_Branch',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='SSC_CGPA',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='SSC_Year',
            field=models.CharField(default='N/A', max_length=255),
        ),
    ]
