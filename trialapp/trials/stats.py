from .models import DockTrial, DockTrialComments
from .filters import DockTrialFilter


#DockTrial stats

def not_started():
    notstr = DockTrial.objects.filter(trial_status='Not Started').count()
    return notstr

def accepted_with_comments():
    return DockTrial.objects.filter(trial_status='Accepted with Comments').count()

def accepted():
    acc = DockTrial.objects.filter(trial_status='Accepted').count()
    return acc

def not_accepted():
    return DockTrial.objects.filter(trial_status='Not accepted').count()

def all_dock_trial():
    return DockTrial.objects.count()
    
#DockTrialComments stats

def close_com():
    return DockTrialComments.objects.filter(status='Close').count()

def open_com():
    return DockTrialComments.objects.filter(status='Open').count()

def all_dock_trial_comments():
    return DockTrialComments.objects.count()

#SeaTrial stats

#SeaTrialComments stats
