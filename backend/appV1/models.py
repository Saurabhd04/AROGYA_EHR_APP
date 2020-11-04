from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    firstName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    gender = models.CharField(max_length = 10)
    dateOfBirth = models.CharField(max_length=10)
    bloodGroup = models.CharField(max_length=3)
    emailId = models.CharField(max_length=50)
    mobileNumber = models.CharField(max_length=10)
    alternateMobileNumber = models.CharField(max_length=10)
    addressLine1 = models.CharField(max_length=50)
    addressLine2 = models.CharField(max_length=50)
    cityOrTown = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin = models.CharField(max_length=6)

