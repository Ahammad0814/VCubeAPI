from django.db import models

# Create your models here.

class LoginData(models.Model):
    Username = models.CharField(max_length=25)
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=25)
    User = models.CharField(max_length=25,default='User')
    Permission = models.CharField(max_length=25,default='Denied')
    
class BatchData(models.Model):
    BatchName = models.CharField(max_length=25)
    Classes = models.CharField(max_length=255,default=0)
    CaseStudies = models.CharField(max_length=255,default=0)
    MockTests = models.CharField(max_length=255,default=0)
    Interviews = models.CharField(max_length=255,default=0)
    
class StudentData(models.Model):
    BatchName = models.CharField(max_length=255,null=True)
    JoiningDate = models.CharField(max_length=255,null=True)
    Name = models.CharField(max_length=255,null=True)
    Phone = models.CharField(max_length=255,null=True)
    Email = models.CharField(max_length=255,null=True)
    PG = models.CharField(max_length=255,null=True,default='N/A')
    PG_Branch = models.CharField(max_length=255,default='N/A')
    PG_CGPA = models.CharField(max_length=255,default='N/A')
    PG_Year = models.CharField(max_length=255,default='N/A')
    Degree = models.CharField(max_length=255,default='N/A')
    Degree_Branch = models.CharField(max_length=255,default='N/A')
    Degree_CGPA = models.CharField(max_length=255,default='N/A')
    Degree_Year = models.CharField(max_length=255,default='N/A')
    Inter = models.CharField(max_length=255,default='12th')
    Inter_Branch = models.CharField(max_length=255,default='N/A')
    Inter_CGPA = models.CharField(max_length=255,default='N/A')
    Inter_Year = models.CharField(max_length=255,default='N/A')
    SSC = models.CharField(max_length=255,default='10th')
    SSC_Branch = models.CharField(max_length=255,default='N/A')
    SSC_CGPA = models.CharField(max_length=255,default='N/A')
    SSC_Year = models.CharField(max_length=255,default='N/A')
    Classes = models.CharField(max_length=255,default=0)
    CaseStudies = models.CharField(max_length=255,default=0)
    MockTests = models.CharField(max_length=255,default=0)
    Interviews = models.CharField(max_length=255,default=0)
    Project = models.CharField(max_length=255,default='N/A')
    Feedback = models.CharField(max_length=255,default='N/A')
    Status = models.CharField(max_length=255,default='Active')
    StudentFeedback = models.CharField(max_length=255,default='N/A')
    Resume = models.CharField(max_length=255,null=True)
    Image = models.CharField(max_length=255,null=True)
    Github = models.CharField(max_length=255,null=True)
    Linkedin = models.CharField(max_length=255,null=True)
    Authentication = models.CharField(max_length=25,default='Active')

class DateData(models.Model):
    BatchDates = models.CharField(max_length=255)
    
class SendOTP(models.Model):
    Email = models.CharField(max_length=255)
    OTP = models.CharField(max_length=255)