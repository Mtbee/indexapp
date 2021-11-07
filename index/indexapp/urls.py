from django.urls import path
from .views import ProgressIndex, ProgressDetail, ProgressCreate, ProgressUpdate, ProgressDelete, csvdownload

urlpatterns = [
    path("", ProgressIndex.as_view(), name="list"),
    path("detail/<int:pk>", ProgressDetail.as_view(), name="detail"),
    path("create", ProgressCreate.as_view(), name="create"),
    path("update/<int:pk>", ProgressUpdate.as_view(), name="update"),
    path("delete/<int:pk>", ProgressDelete.as_view(), name="delete"),
    path("csv/", csvdownload, name="csv"),
]