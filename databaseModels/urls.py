from django.urls import path
from databaseModels import views

urlpatterns=[
    path('student',views.studentInfo),
    path('student/<int:id>',views.studentInfo)
]