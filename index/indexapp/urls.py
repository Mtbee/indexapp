from django.urls import path
from . import views
from .views import ProgressIndex, ProgressDetail, ProgressCreate, ProgressUpdate, ProgressDelete, Progress_csvdownload, top, RegistrationIndex, RegistrationDetail, RegistrationCreate, RegistrationUpdate, RegistrationDelete, Registration_csvdownload, FoodsIndex, FoodsDetail, FoodsCreate, FoodsUpdate, FoodsDelete, Foods_csvdownload, EstimateIndex, EstimateDetail, EstimateCreate, EstimateUpdate, EstimateDelete, Estimate_csvdownload
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("", views.top, name="top"),

    #製作進行
    path("progress/list", ProgressIndex.as_view(), name="progress_list"),
    path("progress/create", ProgressCreate.as_view(), name="progress_create"),
    path("progress/detail/<int:pk>", ProgressDetail.as_view(), name="progress_detail"),
    path("progress/update/<int:pk>", ProgressUpdate.as_view(), name="progress_update"),
    path("progress/delete/<int:pk>", ProgressDelete.as_view(), name="progress_delete"),
    path("progress/csv/", Progress_csvdownload, name="progress_csv"),

    #TN原料登録
    path("registration/list", RegistrationIndex.as_view(), name="registration_list"),
    path("registration/create", RegistrationCreate.as_view(), name="registration_create"),
    path("registration/detail/<int:pk>", RegistrationDetail.as_view(), name="registration_detail"),
    path("registration/update/<int:pk>", RegistrationUpdate.as_view(), name="registration_update"),
    path("registration/delete/<int:pk>", RegistrationDelete.as_view(), name="registration_delete"),
    path("registration/csv/", Registration_csvdownload, name="registration_csv"),

    #TF原料登録
    path("foods/list", FoodsIndex.as_view(), name="foods_list"),
    path("foods/create", FoodsCreate.as_view(), name="foods_create"),
    path("foods/detail/<int:pk>", FoodsDetail.as_view(), name="foods_detail"),
    path("foods/update/<int:pk>", FoodsUpdate.as_view(), name="foods_update"),
    path("foods/delete/<int:pk>", FoodsDelete.as_view(), name="foods_delete"),
    path("foods/csv/", Foods_csvdownload, name="foods_csv"),
  
    #見積依頼
    path("estimate/list", EstimateIndex.as_view(), name="estimate_list"),
    path("estimate/create", EstimateCreate.as_view(), name="estimate_create"),
    path("estimate/detail/<int:pk>", EstimateDetail.as_view(), name="estimate_detail"),
    path("estimate/update/<int:pk>", EstimateUpdate.as_view(), name="estimate_update"),
    path("estimate/delete/<int:pk>", EstimateDelete.as_view(), name="estimate_delete"),
    path("estimate/csv/", Estimate_csvdownload, name="estimate_csv"),
]

