from django.db import models
class Register(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(primary_key=True,max_length=50)
    password=models.CharField(max_length=50)
    phno=models.CharField(max_length=50)
    desig=models.CharField(max_length=15,default="admin")

    def __str__(self):
        return self.email+","+self.username
class Resume(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    dob=models.DateField()
    linkedin=models.URLField()
    address=models.TextField()
    careerobjective=models.TextField()
    education=models.TextField()
    skills=models.TextField()
    projects=models.TextField()
    certifications=models.TextField()
    def __str__(self):
        return self.fullname


  