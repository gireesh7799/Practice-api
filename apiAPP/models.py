from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator
from datetime import date, datetime

STATUS = (
        ('allowed', 'allowed'),
        ('not_allowed', 'not_allowed'),
    )

emp_choices = (
        ('project_manager','project_manager'),
        ('leadership', 'leadership'),
        ('bidder', 'bidder'),

    )    

class Fields(models.Model):
    code = models.CharField(max_length=120)
    customer_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120, unique=True)
    survey = models.URLField() 
    status = models.CharField(max_length=50, choices=STATUS)
    c_date = models.DateField(auto_now=True, editable=False)
    Emp_type= models.CharField(max_length=50,choices=emp_choices)
    start_date = models.DateField(default='')
    end_date = models.DateField(default='')
    revenue = models.IntegerField(default=0)
    cpi = models.FloatField(default=0)
    completes = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(200),
            MinValueValidator(1)
        ])
    client_contactnumber = models.CharField(max_length=14, validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,13}$',
            message="Contact number must be in the format of '+123456789'. Up to 13 digits allowed.")]
    )

    def __str__(self):
        return self.customer_name
