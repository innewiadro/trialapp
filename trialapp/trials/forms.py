from django import forms
from django.db import models
from .models import DockTrialComments, DockTrial
from accounts.models import Profile


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


class DockTrialCommentsForm(forms.ModelForm):
    class Meta:
        model = DockTrialComments
        fields = "__all__"

        widgets = {
            "editor_profile_sign": forms.TextInput(attrs={"class": "form-control", "value":"", "id": "user-ac",'type' : "hidden"})}
    id = models.BigAutoField(primary_key=True)
    pub_date = models.DateTimeField("date published", null=True)
    name_dock_trial = models.ForeignKey(DockTrial, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    status = models.IntegerField(choices=STATUS_COMMENTS, default=0)
    date_of_last_change = models.DateTimeField(auto_now=True)
    
   
    department = models.IntegerField(choices=DEPARTMENTS, default=10)
    contractor_comment = models.TextField(blank=True)
    design_comment = models.TextField(blank=True)
    shipowner_comment = models.TextField(blank=True)
    description = models.TextField(blank=True)


STATUS_TRIALS = (('Not Started', 'Not Started'),
                 ('Accepted with Comments', 'Accepted with Comments'),
                 ('Accepted', 'Accepted'),
                 ('Not accepted', 'Not accepted'))

class DockTrialForm(forms.ModelForm):
    class Meta:
        model = DockTrial
        fields = "__all__"

    
    trial_name = models.CharField(max_length=255, null=True)
    trial_number = models.CharField(max_length=5, null=True)
    trial_status = models.CharField(choices=STATUS_TRIALS, default='Not Started',max_length=155)
    specification = models.TextField(blank=True)
