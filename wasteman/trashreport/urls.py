from django.urls import path
from . import views

app_name = 'trashreport'

urlpatterns = [
    path('report/', views.report_trash, name='report_trash'),
    path('reports/', views.TrashReportListView.as_view(), name='trash_report_list'),
    path('reports/<int:pk>/', views.TrashReportDetailView.as_view(), name='trash_report_detail'),
]
