# Generated by Django 5.0.2 on 2024-06-26 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0002_delete_student_files_data_studentdata_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='CaseStudies',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Classes',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Degree',
            field=models.CharField(default='N/A', max_length=25),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Degree_Branch',
            field=models.CharField(default='N/A', max_length=25),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Degree_CGPA',
            field=models.CharField(default='N/A', max_length=25),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Degree_Year',
            field=models.CharField(default='N/A', max_length=25),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Feedback',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Inter',
            field=models.CharField(default='12th', max_length=25),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Inter_Branch',
            field=models.CharField(default='N/A', max_length=25),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Inter_CGPA',
            field=models.CharField(default='N/A', max_length=25),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Inter_Year',
            field=models.CharField(default='N/A', max_length=25),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Interviews',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='MockTests',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='PG',
            field=models.CharField(default='N/A', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='PG_Branch',
            field=models.CharField(default='N/A', max_length=25),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='PG_CGPA',
            field=models.CharField(default='N/A', max_length=25),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='PG_Year',
            field=models.CharField(default='N/A', max_length=25),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Project',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='SSC',
            field=models.CharField(default='10th', max_length=25),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='SSC_Branch',
            field=models.CharField(default='N/A', max_length=25),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='SSC_CGPA',
            field=models.CharField(default='N/A', max_length=25),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='SSC_Year',
            field=models.CharField(default='N/A', max_length=25),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Status',
            field=models.CharField(default='Active', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='StudentFeedback',
            field=models.CharField(default='N/A', max_length=255),
        ),
    ]
