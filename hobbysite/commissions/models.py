from datetime import datetime
from django.db import models
from django.urls import reverse
from user_management.models import Profile


class Commission(models.Model):
    
    class StatusChoices(models.IntegerChoices):
        OPEN = 1, "Open"
        FULL = 2, "Full"
        COMPLETED = 3, "Completed"
        DISCONTINUED = 4, "Discontinued"

    title = models.CharField(max_length = 255)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='author')
    description = models.TextField(null = False)
    status = models.PositiveSmallIntegerField(
        choices = StatusChoices.choices,
        default = StatusChoices.OPEN
        )
    created_on = models.DateField(null = False, auto_now_add = True)
    updated_on = models.DateField(null = False, auto_now = True)


    class Meta:
        ordering = ['status', '-created_on']
    
    
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("commissions:commissions_detail", args=str(self.pk))


    def job_checker (self):
        if all(job.status == 2 for job in self.commissions.all()):
            self.status = '2'
            self.save()
            return str("Full")
        else:
            self.status = 1
            self.save()
            return str("Open")

class Job(models.Model):

    class StatusChoices(models.IntegerChoices):
        OPEN = 1, "Open"
        FULL = 2, "Full"
        

    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name='commissions')
    role = models.CharField(max_length = 255)
    manpower_required = models.IntegerField()
    status = models.PositiveSmallIntegerField(
		choices = StatusChoices.choices,
		default = StatusChoices.OPEN,
        )
    

    class Meta:
        ordering = ['status', '-manpower_required', 'role']

        
    def __str__(self):
        return str(self.role)
    
    def number_of_accepted_applicants(self):
        accepted_applicants = self.job_application.filter(status = '2').count() #detects number of accepted
        manpower_required = self.manpower_required
        open_slots = manpower_required - accepted_applicants
        if open_slots == 0:
            self.status ='2'
            self.save()
        else:
            self.status = 1
            self.save()
        return  open_slots

class JobApplication(models.Model):

    class StatusChoices(models.IntegerChoices):
        PENDING = 1, "Pending"
        ACCEPTED = 2, "Accepted"
        REJECTED = 3, "Rejected"

	
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_application')
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='applicant')
    status = models.PositiveSmallIntegerField(
		choices = StatusChoices.choices,
		default = StatusChoices.PENDING,
        )
    applied_on = models.DateField(null = False, auto_now_add = True)
	
    class Meta:
        ordering = ['status', '-applied_on']

    
    def __str__(self):
        return str(self.job)