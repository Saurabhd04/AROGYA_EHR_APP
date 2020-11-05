from django.db import models
from django import forms
# Create your models here.
class PersonalInfo(models.Model):
    firstName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100,null=True)
    lastName = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length = 10)
    dateOfBirth = models.DateField(max_length=10)

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('AB+', 'AB+'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
        ('O-', 'O-'),
        ('O+', 'O+'),
    ]
    bloodGroup = models.CharField(
        max_length=3,
        choices=BLOOD_GROUP_CHOICES,
        null=True
    )

    emailId = models.EmailField(max_length=50, unique=True)
    mobileNumber = models.CharField(max_length=10)
    alternateMobileNumber = models.CharField(max_length=10, null = True)
    addressLine1 = models.CharField(max_length=50)
    addressLine2 = models.CharField(max_length=50)
    cityOrTown = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin = models.CharField(max_length=6)

class EmergencyInfo(models.Model):                                      
    relativeName = models.CharField(max_length=100)
    relationship = models.CharField(max_length=20)
    primaryMobileNumber = models.CharField(max_length=10)
    secondaryMobileNumber = models.CharField(max_length=10, null = True)
    relativeAddress = models.CharField(max_length=100)
    userId = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

class InsuranceInfo(models.Model):
    insuranceProvider = models.CharField(max_length=50)
    policyNumber = models.CharField(max_length=20, unique=True)
    policyName = models.CharField(max_length=50)
    validTill = models.DateField()
    userId = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

