from django.db import models
from django.urls import reverse
from django.utils import timezone

  
GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

KNOWN_LANGUAGES =( 
    ("1", "Tamil"), 
    ("2", "English"), 
    ("3", "Hindi") 
) 

CITY_CHOICES =( 
    ("1", "Tirupur"), 
    ("2", "Coimbatore"), 
    ("3", "Chennai") 
) 

STATE_CHOICES =( 
    ("1", "TamilNadu"), 
    ("2", "Karnataka"), 
    ("3", "Kerala"),
    ("4", "Andhra Pradesh") 
) 

class Student(models.Model):
    name = models.CharField(max_length= 50,editable=True)
    dateofbirth = models.DateField(default=timezone.now)
    emailid = models.EmailField((""), max_length=254,default="example@gmail.com",editable=True)
    mobile = models.CharField(max_length=10, unique=True,default="9123456789",editable=True)
    gender = models.CharField(choices=GENDER_CHOICES, default="Male",max_length=128,editable=True)
    address = models.TextField(max_length=200,default="Tirupur",editable=True)
    city=models.CharField(max_length=200,choices=CITY_CHOICES,default="Tirupur")
    state=models.CharField(max_length=20,choices=STATE_CHOICES,editable=True,default="Tamil Nadu")
    pincode = models.CharField(("pincode"), max_length=6, default="641604",editable=True)
     

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student:student_edit', kwargs={'pk': self.pk})
