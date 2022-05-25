from django.urls import path
from . import views
from .views import (top,
ProgressIndex, ProgressDetail, ProgressCreate, ProgressUpdate, ProgressDelete, Progress_csvdownload,
RegistrationIndex, RegistrationDetail, RegistrationCreate, RegistrationUpdate, RegistrationDelete, Registration_csvdownload,
FoodsIndex, FoodsDetail, FoodsCreate, FoodsUpdate, FoodsDelete, Foods_csvdownload,
SendRequestIndex, SendRequestDetail, SendRequestCreate, SendRequestUpdate, SendRequestDelete, SendRequest_csvdownload,
ReceiveRequestIndex, ReceiveRequestDetail, ReceiveRequestCreate, ReceiveRequestUpdate, ReceiveRequestDelete, ReceiveRequest_csvdownload,
RouletteIndex, RouletteCreate, RouletteDelete)
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
  
    #物品サービス依頼(発信)
    path("sendrequest/list", SendRequestIndex.as_view(), name="sendrequest_list"),
    path("sendrequest/create", SendRequestCreate.as_view(), name="sendrequest_create"),
    path("sendrequest/detail/<int:pk>", SendRequestDetail.as_view(), name="sendrequest_detail"),
    path("sendrequest/update/<int:pk>", SendRequestUpdate.as_view(), name="sendrequest_update"),
    path("sendrequest/delete/<int:pk>", SendRequestDelete.as_view(), name="sendrequest_delete"),
    path("sendrequest/csv/", SendRequest_csvdownload, name="sendrequest_csv"),


    #物品サービス依頼(受信)
    path("receiverequest/list", ReceiveRequestIndex.as_view(), name="receiverequest_list"),
    path("receiverequest/create", ReceiveRequestCreate.as_view(), name="receiverequest_create"),
    path("receiverequest/detail/<int:pk>", ReceiveRequestDetail.as_view(), name="receiverequest_detail"),
    path("receiverequest/update/<int:pk>", ReceiveRequestUpdate.as_view(), name="receiverequest_update"),
    path("receiverequest/delete/<int:pk>", ReceiveRequestDelete.as_view(), name="receiverequest_delete"),
    path("receiverequest/csv/", ReceiveRequest_csvdownload, name="receiverequest_csv"),

        #ルーレット
    path("roulette/list", RouletteIndex.as_view(), name="roulette_list"),
    path("roulette/create", RouletteCreate.as_view(), name="roulette_create"),
    path("roulette/delete/<int:pk>", RouletteDelete.as_view(), name="roulette_delete"),
]