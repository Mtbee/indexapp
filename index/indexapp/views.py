from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Progress
from django.http import HttpResponse
import csv

# Create your views here.
class ProgressIndex(ListView):
    model = Progress
    context_object_name = "progress"
    ordering = ["-number"]

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class ProgressDetail(DetailView):
    model = Progress
    context_object_name = "Progress"

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class ProgressCreate(CreateView):
    model = Progress
    fields = "__all__"
    success_url = reverse_lazy("list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class ProgressUpdate(UpdateView):
    model = Progress
    fields = "__all__"
    success_url = reverse_lazy("list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class ProgressDelete(DeleteView):
    model = Progress
    context_object_name = "progress"
    success_url = reverse_lazy("list")

    def get(self, request, pk):
        # スーパーユーザーでなければログインページ
        if not self.request.user.is_superuser:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

def csvdownload(request):
    response = HttpResponse(content_type="text/csv; charset=cp932")
    response['Content-Disposition'] = 'attachment; filename = index.csv'
    writer = csv.writer(response)
    writer.writerow([
        "No.",
        "コード",
        "品名",
        "数量",
        "単位",
        "発注日",
        "希望納期",
        "確定納期",
        "備考",
    ])
    for post in Progress.objects.all():
        writer.writerow([
            post.number,
            post.code,
            post.name,
            post.quantity,
            post.unit,
            post.order,
            post.prefer,
            post.fixed,
            post.description])
    return response
