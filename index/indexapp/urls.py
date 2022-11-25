from operator import index
from django.urls import path
from . import views
from .views import (top,
ProgressNBIndex, ProgressNBDetail, ProgressNBCreate, ProgressNBUpdate, ProgressNBDelete, ProgressNB_csvdownload,
ProgressPBIndex, ProgressPBDetail, ProgressPBCreate, ProgressPBUpdate, ProgressPBDelete, ProgressPB_csvdownload,
RegistrationIndex, RegistrationDetail, RegistrationCreate, RegistrationUpdate, RegistrationDelete, Registration_csvdownload,
FoodsIndex, FoodsDetail, FoodsCreate, FoodsUpdate, FoodsDelete, Foods_csvdownload,
SendRequestIndex, SendRequestDetail, SendRequestCreate, SendRequestUpdate, SendRequestDelete, SendRequest_csvdownload,
ReceiveRequestIndex, ReceiveRequestDetail, ReceiveRequestCreate, ReceiveRequestUpdate, ReceiveRequestDelete, ReceiveRequest_csvdownload,
RouletteIndex, RouletteCreate, RouletteDelete, index)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("", views.top, name="top"),

    #製作進行NB
    path("progressnb/list", ProgressNBIndex.as_view(), name="progressnb_list"),
    path("progressnb/create", ProgressNBCreate.as_view(), name="progressnb_create"),
    path("progressnb/detail/<int:pk>", ProgressNBDetail.as_view(), name="progressnb_detail"),
    path("progressnb/update/<int:pk>", ProgressNBUpdate.as_view(), name="progressnb_update"),
    path("progressnb/delete/<int:pk>", ProgressNBDelete.as_view(), name="progressnb_delete"),
    path("progressnb/csv/", ProgressNB_csvdownload, name="progressnb_csv"),

    #製作進行PB
    path("progresspb/list", ProgressPBIndex.as_view(), name="progresspb_list"),
    path("progresspb/create", ProgressPBCreate.as_view(), name="progresspb_create"),
    path("progresspb/detail/<int:pk>", ProgressPBDetail.as_view(), name="progresspb_detail"),
    path("progresspb/update/<int:pk>", ProgressPBUpdate.as_view(), name="progresspb_update"),
    path("progresspb/delete/<int:pk>", ProgressPBDelete.as_view(), name="progresspb_delete"),
    path("progresspb/csv/", ProgressPB_csvdownload, name="progresspb_csv"),

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

    #パッカー
    path("packer", index, name="packers"),
]