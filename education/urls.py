
from . import views
from django.urls import path

app_name = "education"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>', views.detail, name="detail"),
]