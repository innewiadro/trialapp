from django.db import models
from accounts.models import Profile, User

STATUS_TRIALS = (('Not Started', 'Not Started'),
                 ('Accepted with Comments', 'Accepted with Comments'),
                 ('Accepted', 'Accepted'),
                 ('Not accepted', 'Not accepted'))
                 


class DockTrial(models.Model):
    trial_name = models.CharField(max_length=200)
    trial_number = models.CharField(max_length=5, null=True)
    trial_status = models.CharField(choices=STATUS_TRIALS, default='Not Started', max_length=155)
    specification = models.TextField(null=True)

    def __str__(self):
        return f"{self.trial_name}"

    
    class Meta:
        db_table= "docktrials"


STATUS_COMMENTS = (('Open', 'Open'),
                   ('Close', 'Close'))

DEPARTMENTS = (("Hull Production Department", 'HPD'),
               ('Piping Department', 'PID'),
               ('Outfitting Department', 'OD'),
               ('Electric Deepartment', 'ED'),
               ('Commissioning Department', 'CD'),
               ('Quality Control Department', 'QCD'),
               ('Purchasing and Logistics Deparment', 'P&L'),
               ('Painting Department', 'PD'),
               ('Design Office', 'DO'),
               ('Service', 'S'),
               ('Construction Office', 'CO'))


class DockTrialComments(models.Model):
    id = models.BigAutoField(primary_key=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    name_dock_trial = models.ForeignKey(DockTrial, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    status = models.CharField(choices=STATUS_COMMENTS, default='Open', max_length=100)
    date_of_last_change = models.DateTimeField(auto_now=True)
    
    
    editor_profile_sign = models.TextField(blank=True)
    department = models.CharField(choices=DEPARTMENTS, default='Construction Office', max_length=100)
    contractor_comment = models.TextField(blank=True)
    design_comment = models.TextField(blank=True)
    shipowner_comment = models.TextField(blank=True)
    description = models.TextField(null=True)
    

    def __str__(self):
        return f"{self.name}"


    
    
    
