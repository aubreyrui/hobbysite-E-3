from datetime import datetime
from django.db import models
from django.urls import reverse
from user_management.models import Profile


class Commission(models.Model):
    STATUS_OPTIONS = ( # https://stackoverflow.com/questions/18676156/how-to-properly-use-the-choices-field-option-in-django
        ('OPEN', "Open"),
        ('FULL', "Full"),
		('COMPLETED', "Completed"),
		('DISCONTINUED', "Discontinued"),
    )
    title = models.CharField(max_length = 255)
    description = models.TextField(null = False)
    status = models.CharField(max_length = 12,
								choices = STATUS_OPTIONS,
								default = 'OPEN')
    people_required = models.IntegerField(null = False)
    created_on = models.DateField(null = False, auto_now_add = True)
    updated_on = models.DateField(null = False, auto_now = True)


    class Meta:
        ordering = ['created_on']
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("commissions:commissions_detail", args=str(self.pk))


class Job(models.Model):
    STATUS_OPTIONS = (
		('OPEN', "Open"),
		('FULL', "Full"),
	)

    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name='commissions')
    role = models.CharField(max_length = 255)
    manpower_required = models.IntegerField()
    status = models.CharField(max_length = 4,
								choices = STATUS_OPTIONS,
								default = 'OPEN')
    

    class Meta:
        ordering = ['status', '-manpower_required', 'role']

        
    def __str__(self):
        return self.commission
    

class JobApplication(models.Model):
    STATUS_OPTIONS = (
		('PENDING', "Pending"),
		('ACCEPTED', "Accepted"),
		('REJECTED', "Rejected"),
	)
	
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job')
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    status = models.CharField(max_length = 8,
								choices = STATUS_OPTIONS,
								default = 'PENDING')
    applied_on = models.DateField(null = False, auto_now_add = True)
	
    class Meta:
        ordering = ['-applied_on'] # add priority for status

    def status_priority (self): # find sources
	    status_order = {
			"Pending" : 1,
			"Accepted" : 2,
			"Rejected" : 3,
		}
        # return status_order.get(self.status, 0)