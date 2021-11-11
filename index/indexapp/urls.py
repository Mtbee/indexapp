from django.urls import path
from .views import ProgressIndex, ProgressDetail, ProgressCreate, ProgressUpdate, ProgressDelete, csvdownload
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", ProgressIndex.as_view(), name="list"),
    path("detail/<int:pk>", ProgressDetail.as_view(), name="detail"),
    path("create", ProgressCreate.as_view(), name="create"),
    path("update/<int:pk>", ProgressUpdate.as_view(), name="update"),
    path("delete/<int:pk>", ProgressDelete.as_view(), name="delete"),
    path("csv/", csvdownload, name="csv"),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]