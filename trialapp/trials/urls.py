from django.urls import path

from . import views
from .views import DockTrialCommentsList, DockTrialCommentsCreateView, DockTrialCommentsDeleteView
from .views import DockTrialCommentsUpdateView, DockTrialCommentsDetailView, DockTrialDetailView
from .views import DockTrialList, DockTrialCreateView, DockTrialUpdateView, DockTrialDeleteView



urlpatterns = [path("", DockTrialList.as_view(), name='trials'),
               path("<slug:pk>", DockTrialDetailView.as_view(), name="dock-trial-detail"),
               path("new/", DockTrialCreateView.as_view(), name='trial-create'),
               path("<slug:pk>/edit", DockTrialUpdateView.as_view(), name="trial-update"),
               path("<slug:pk>/delete", DockTrialDeleteView.as_view(), name="trial-delete"),
               # komentarze
               path("dock-comments/", DockTrialCommentsList.as_view(), name='dock-comments'),
               path("dock-comments/<int:id>/", DockTrialCommentsDetailView.as_view(), name='docktrialcomments-detail'),
               path("dock-comments/new", DockTrialCommentsCreateView.as_view(), name="dock-comment-create"),
               path("dock-comments/<slug:pk>/edit", DockTrialCommentsUpdateView.as_view(), name="dock-comment-update"),
               path("dock-comments/<slug:pk>/delete", DockTrialCommentsDeleteView.as_view(), name="dock-comment-delete"),
               path("filter-trial/", views.search_docktrial , name='trial-filter'),
               path("filter-comments/", views.search_docktrial_comments, name='trial-comments-filter'),
               path("export-docktrial-csv/", views.export_docktrial_to_csv, name='export-trial'),
               path("export-docktrial-comments-csv/", views.export_docktrialcommments_to_csv, name='export-trial-comments')
                              
]
