# Generated by Django 5.0.2 on 2024-06-25 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatchData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BatchName', models.CharField(max_length=25)),
                ('Classes', models.CharField(default=0, max_length=255)),
                ('CaseStudies', models.CharField(default=0, max_length=255)),
                ('MockTests', models.CharField(default=0, max_length=255)),
                ('Interviews', models.CharField(default=0, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DateData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BatchDates', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LoginData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=25)),
                ('Email', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=25)),
                ('User', models.CharField(default='User', max_length=25)),
                ('Permission', models.CharField(default='Denied', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='SendOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=255)),
                ('OTP', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Files_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StdId', models.IntegerField(null=True)),
                ('Resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('Image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BatchName', models.CharField(max_length=25, null=True)),
                ('JoiningDate', models.CharField(max_length=25, null=True)),
                ('Name', models.CharField(max_length=25, null=True)),
                ('Phone', models.CharField(max_length=25, null=True)),
                ('Email', models.CharField(max_length=25, null=True)),
                ('PG', models.CharField(max_length=25, null=True)),
                ('PG_Branch', models.CharField(max_length=25, null=True)),
                ('PG_CGPA', models.CharField(max_length=25, null=True)),
                ('PG_Year', models.CharField(max_length=25, null=True)),
                ('Degree', models.CharField(max_length=25, null=True)),
                ('Degree_Branch', models.CharField(max_length=25, null=True)),
                ('Degree_CGPA', models.CharField(max_length=25, null=True)),
                ('Degree_Year', models.CharField(max_length=25, null=True)),
                ('Inter', models.CharField(max_length=25, null=True)),
                ('Inter_Branch', models.CharField(max_length=25, null=True)),
                ('Inter_CGPA', models.CharField(max_length=25, null=True)),
                ('Inter_Year', models.CharField(max_length=25, null=True)),
                ('SSC', models.CharField(max_length=25, null=True)),
                ('SSC_Branch', models.CharField(max_length=25, null=True)),
                ('SSC_CGPA', models.CharField(max_length=25, null=True)),
                ('SSC_Year', models.CharField(max_length=25, null=True)),
                ('Classes', models.CharField(max_length=255, null=True)),
                ('CaseStudies', models.CharField(max_length=255, null=True)),
                ('MockTests', models.CharField(max_length=255, null=True)),
                ('Interviews', models.CharField(max_length=255, null=True)),
                ('Project', models.CharField(max_length=255, null=True)),
                ('Feedback', models.CharField(max_length=255, null=True)),
                ('Status', models.CharField(max_length=255, null=True)),
                ('StudentFeedback', models.CharField(default='N/A', max_length=255, null=True)),
            ],
        ),
    ]
