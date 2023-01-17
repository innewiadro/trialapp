from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.template import loader
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView, DeleteView, UpdateView
from .models import DockTrialComments, DockTrial
from .forms import DockTrialCommentsForm, DockTrialForm
from .filters import DockTrialFilter, DockTrialCommentsFilter
from .stats import not_started, accepted_with_comments, accepted, not_accepted, close_com, open_com, all_dock_trial, all_dock_trial_comments
from django.core.paginator import Paginator
import unicodecsv as csv

def index(request):
    template = loader.get_template("base.html")
    return HttpResponse(template.render())

def hello(request):
    template = loader.get_template("hello.html")
    return HttpResponse(template.render())


# DockTrialComments Views

class DockTrialCommentsDetailView(DetailView):
    template_name = "docktrialcomments_detail.html"
    queryset = DockTrialComments.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(DockTrialComments, id = id)
    

class DockTrialCommentsList(ListView):
    model = DockTrialComments
    template_name = "dock_trial_comments_list.html"
    paginate_by = 10
    
    def get_context_data(self, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list
        form = DockTrialCommentsForm(self.request.GET)
        return super().get_context_data(
            form = form,
            object_list=queryset,
            close_com=close_com(),
            open_com=open_com(),
            all_dock_trial_comments=all_dock_trial_comments(),
            **kwargs)


def search_docktrial_comments(request):
    dock_trial_comments_list = DockTrialComments.objects.all()
    dock_trial_comments_filter = DockTrialCommentsFilter(request.GET, queryset=dock_trial_comments_list)
    
   
    return render(request, 'dock_trial_comments_filter_list.html', {'filter': dock_trial_comments_filter})
  
class DockTrialCommentsUpdateView(UpdateView):
    form_class = DockTrialCommentsForm
    model = DockTrialComments
    template_name = "dock_trial_comments_edit.html"
    success_url = reverse_lazy("dock-comments")
    
    
class DockTrialCommentsCreateView(CreateView):
    form_class = DockTrialCommentsForm
    model = DockTrialComments
    template_name = "dock_trial_comments_form.html"
    
    success_url = reverse_lazy("dock-comments")


class DockTrialCommentsFormView(FormView):
    template_name = "docktrialcomments_forms.html"
    from_class = DockTrialCommentsForm


class DockTrialCommentsDeleteView(DeleteView):
    template_name = "dock_trial_comment_delete.html"
    model = DockTrialComments
    success_url = reverse_lazy("dock-comments")


def export_docktrialcommments_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="docktrial-comments.csv"'

    
    writer = csv.writer(response, delimiter=";", encoding='utf-8-sig')
    writer.writerow(['id', 'public date', 'Trial Name', 'name', 'Status', 'last change date', 'editor', 'department', 'contractor comments', 'design comments', 'shipowner comments', 'description'])
    trials = DockTrialComments.objects.all().values_list('id', 'pub_date', 'name_dock_trial', 'name', 'status', 'date_of_last_change',
                                                         'editor_profile_sign', 'department', 'contractor_comment', 'design_comment', 'shipowner_comment', 'description')

    for trial in trials:
        writer.writerow(trial)
        
    return response

# DockTrial Views

def export_docktrial_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="docktrials.csv"'

    
    writer = csv.writer(response, delimiter=";", encoding='utf-8-sig')
    writer.writerow(['id', 'Trial Number', 'Trial Name', 'Description', 'Status'])
    trials = DockTrial.objects.all().values_list('id', 'trial_number', 'trial_name', 'specification', 'trial_status')

    for trial in trials:
        writer.writerow(trial)
        
    return response

class DockTrialList(ListView):
    model = DockTrial
    context_object_name = "trials"
    template_name = "dock_trial_list.html"
    paginate_by = 10
    
    def get_context_data(self, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list
        form = DockTrialForm(self.request.GET)
        return super().get_context_data(
            form=form,
            object_list=queryset,
            not_started=not_started(),
            accepted=accepted(),
            accepted_with_comments=accepted_with_comments(),
            not_accepted=not_accepted(),
            all_dock_trial=all_dock_trial(),
            **kwargs)

    
def search_docktrial(request):
    dock_trial_list = DockTrial.objects.all()
    dock_trial_filter = DockTrialFilter(request.GET, queryset=dock_trial_list)
    
    
    return render(request, 'dock_trial_filter_list.html', {'filter': dock_trial_filter})

    
class DockTrialFormView(FormView):
    template_name = "dock_trial_form.html"
    form_class = DockTrialForm


class DockTrialCreateView(CreateView):
    model = DockTrial
    template_name = "dock_trial_add.html"
    fields = '__all__'
    success_url = reverse_lazy("trials")

    
class DockTrialDetailView(DetailView):
    template_name = "dock_trial_detail.html"
    model = DockTrial
    context_object_name = "name_dock_trials"

    def get_context_data(self, **kwargs):
        """return super().get_context_data(comments_list = DockTrialComments.objects.filter(name_dock_trial=2), **kwargs)"""
        context = super().get_context_data(**kwargs)
        context["comments"] = DockTrialComments.objects.filter(name_dock_trial=self.get_object())
        print(context)
        return context


class DockTrialUpdateView(UpdateView):
    form_class = DockTrialForm
    model = DockTrial
    template_name = "dock_trial_edit.html"
    success_url = reverse_lazy("trials")
    

class DockTrialDeleteView(DeleteView):
    template_name = "dock_trial_delete.html"
    model = DockTrial
    success_url = reverse_lazy("trials")

