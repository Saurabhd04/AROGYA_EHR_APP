from django.db import models
from django import forms
from django.contrib.postgres.fields import ArrayField
import datetime

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
    aadhaarCardNumber = models.CharField(max_length=14, null=True)

class EmergencyInfo(models.Model):                                      
    relativeName = models.CharField(max_length=100)
    relationship = models.CharField(max_length=20)
    primaryContactNumber = models.CharField(max_length=10)
    secondaryContactNumber = models.CharField(max_length=10, null = True)
    relativeAddress = models.CharField(max_length=100)
    userId = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

class InsuranceInfo(models.Model):
    insuranceProvider = models.CharField(max_length=50)
    policyNumber = models.CharField(max_length=20, unique=True)
    policyName = models.CharField(max_length=50)
    validTill = models.DateField()
    userId = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)    
    
class OrganizationInfo(models.Model):
    #organization must not be deleted
    orgName = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    ACTIVE_CHOICES = [
        ("Y","YES"),
        ("N", "NO")
    ]
    activeIndicator = models.CharField(max_length=1, choices=ACTIVE_CHOICES)
    orgRegNumber = models.CharField(max_length=26, unique=True)

class MedicalPractitionerInfo(models.Model):
    name = models.CharField(max_length=30)
    licenseNumber = models.CharField(max_length=20)
    profile = models.CharField(max_length=20)
    mobileNumber = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    ACTIVE_CHOICES = [
        ("Y","YES"),
        ("N", "NO")
    ]
    activeIndicator = models.CharField(max_length=1, choices=ACTIVE_CHOICES)
    orgId = models.ForeignKey(OrganizationInfo, null= True, on_delete = models.SET_NULL)

class PrescriptionInfo(models.Model):
    ADDED_BY_CHOICES = [
        ('Self', 'User'),
        ('Doctor', 'Doctor'),
    ]
    addedBy = models.CharField(
        max_length=6,
        choices=ADDED_BY_CHOICES,
    )
    prescriberId = models.ForeignKey(MedicalPractitionerInfo, null = True, on_delete=models.SET_NULL)
    hospitalOrClinic = models.CharField(max_length=50, null = True) # fetched from MP table
    doctorName = models.CharField(max_length=20, null = True)  # fetched from MP Table
    prescriptionDate = models.DateField(default= datetime.date.today)  
    contactNumber = models.CharField(max_length=10, null=True) # fetched from MP table
    address = models.CharField(max_length=50, null=True) # fetched from MP table
    symptoms = models.TextField(max_length=255, null=True)
    medicines = models.TextField(max_length=255, null=True) #put this field comma seperated
    notes = models.CharField(max_length=255, null=True)
    prescriptionAttachment = models.ImageField(null = True)
    userId = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    
    #Automatically filling fields when prescriber id is provided.
    def save(self, *args, **kwargs):
        if not self.id and self.prescriberId is not None:
            MP = MedicalPractitionerInfo.objects.get(id = self.prescriberId.__dict__['id'])
            org = OrganizationInfo.objects.get(id=MP.__dict__['orgId_id'])

            self.hospitalOrClinic = org.__dict__['orgName']
            self.address = org.__dict__['address']
            self.doctorName = self.prescriberId.__dict__['name']
            self.contactNumber = self.prescriberId.__dict__['mobileNumber']
        super(PrescriptionInfo, self).save()


class BloodPressure(models.Model):
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    date = models.DateField(default = datetime.date.today)
    notes = models.CharField(max_length=255, null = True)
    userId = models.ForeignKey(PersonalInfo, on_delete = models.CASCADE)