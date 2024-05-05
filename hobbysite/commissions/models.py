from datetime import datetime
from django.db import models
from django.urls import reverse
from user_management.models import Profile
from django.utils.translation import gettext_lazy as _


class Commission(models.Model):
    
    class StatusChoices(models.IntegerChoices):
        OPEN = 1, "Open"
        FULL = 2, "Full"
        COMPLETED = 3, "Completed"
        DISCONTINUED = 4, "Discontinued"

    
    title = models.CharField(max_length = 255)
    description = models.TextField(null = False)
    status = models.PositiveSmallIntegerField(
        choices = StatusChoices.choices,
        default = StatusChoices.OPEN,
        )
    people_required = models.IntegerField(null = False)
    created_on = models.DateField(null = False, auto_now_add = True)
    updated_on = models.DateField(null = False, auto_now = True)


    class Meta:
        ordering = ['status', 'created_on']
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("commissions:commissions_detail", args=str(self.pk))


class Job(models.Model):
    STATUS_CHOICES = {
		0: "Open",
		1: "Full",
    }

    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name='commissions')
    role = models.CharField(max_length = 255)
    manpower_required = models.IntegerField()
    status = models.CharField(
        max_length = 4,
		choices = STATUS_CHOICES.items(),
		default = 0,
        )
    

    class Meta:
        ordering = ['status', '-manpower_required', 'role']

        
    def __str__(self):
        return self.commission
    

class JobApplication(models.Model):
    STATUS_CHOICES = {
		"PENDING": "Pending",
		"ACCEPTED": "Accepted",
		"REJECTED": "Rejected",
    }
	
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job')
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    status = models.CharField(
        max_length = 8,
		choices = STATUS_CHOICES.items(),
		default = "PENDING",
        )
    applied_on = models.DateField(null = False, auto_now_add = True)
	
    class Meta:
        ordering = ['-applied_on'] # add priority for status

    def status_priority (self): 
	    status_order = {
			"Pending" : 1,
			"Accepted" : 2,
			"Rejected" : 3,
		}
        # return status_order.get(self.status, 0)