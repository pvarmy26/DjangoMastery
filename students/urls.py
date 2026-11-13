from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("upload/",views.upload_document,name="upload_document"),
    path("api/students/", views.student_api, name="student_api"),
    path("api/students/<int:pk>/",views.student_detail_api,name="student_detail_api"),
    path("api/admin/", views.admin_api, name="admin_api"),
]