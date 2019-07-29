from django.urls import path, include
from attendance import views

app_name = 'attendance'

urlpatterns = [
    path('', views.attend, name="attend"),
    path('attendance/<int:status_id>/', views.result, name="result"),
    path('attendance/state/', views.state, name="state")
]