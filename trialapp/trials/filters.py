from .models import DockTrialComments, DockTrial
import django_filters

class DockTrialCommentsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")
    pub_date = django_filters.DateFilter(lookup_expr="icontains")
    date_of_last_change = django_filters.DateFilter(lookup_expr="icontains")
    
    class Meta:
        model = DockTrialComments
        fields = ["id", "name_dock_trial", "status", "department", "name"]

        
class DockTrialFilter(django_filters.FilterSet):
    trial_name = django_filters.CharFilter(lookup_expr="icontains")
    trial_number = django_filters.CharFilter(lookup_expr="icontains")
    
    class Meta:
        model = DockTrial
        fields = ["trial_status"]
