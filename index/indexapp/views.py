from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Progress, Registration, Foods
from django.http import HttpResponse
import csv

def top(request):
    return render(request, 'top.html')

# 制作進行
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
    success_url = reverse_lazy("list")

    def get(self, request, pk):
        # スーパーユーザーでなければログインページ
        if not self.request.user.is_superuser:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

def Progress_csvdownload(request):
    response = HttpResponse(content_type="text/csv; charset=cp932")
    response['Content-Disposition'] = 'attachment; filename = progress_index.csv'
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





# TN原料登録
class RegistrationIndex(ListView):
    model = Registration
    context_object_name = "registration"
    ordering = ["-number"]

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class RegistrationDetail(DetailView):
    model = Registration

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class RegistrationCreate(CreateView):
    model = Registration
    fields = "__all__"
    success_url = reverse_lazy("registration_list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class RegistrationUpdate(UpdateView):
    model = Registration
    fields = "__all__"
    success_url = reverse_lazy("registration_list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class RegistrationDelete(DeleteView):
    model = Registration
    success_url = reverse_lazy("registration_list")

    def get(self, request, pk):
        # スーパーユーザーでなければログインページ
        if not self.request.user.is_superuser:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

def Registration_csvdownload(request):
    response = HttpResponse(content_type="text/csv; charset=cp932")
    response['Content-Disposition'] = 'attachment; filename = TN_registration_index.csv'
    writer = csv.writer(response)
    writer.writerow([
        "No.",
        "コード",
        "品名",
        "備考",
        
    ])
    for post in Registration.objects.all():
        writer.writerow([
            post.number,
            post.code,
            post.name,
            post.description])
    return response


# TF原料登録
class FoodsIndex(ListView):
    model = Foods
    context_object_name = "foods"
    ordering = ["-number"]

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class FoodsDetail(DetailView):
    model = Foods

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class FoodsCreate(CreateView):
    model = Foods
    fields = "__all__"
    success_url = reverse_lazy("foods_list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class FoodsUpdate(UpdateView):
    model = Foods
    fields = "__all__"
    success_url = reverse_lazy("foods_list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class FoodsDelete(DeleteView):
    model = Foods
    success_url = reverse_lazy("foods_list")

    def get(self, request, pk):
        # スーパーユーザーでなければログインページ
        if not self.request.user.is_superuser:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

def Foods_csvdownload(request):
    response = HttpResponse(content_type="text/csv; charset=cp932")
    response['Content-Disposition'] = 'attachment; filename = TF_registration_index.csv'
    writer = csv.writer(response)
    writer.writerow([
        "No.",
        "コード",
        "品名",
        "備考",
        
    ])
    for post in Foods.objects.all():
        writer.writerow([
            post.number,
            post.code,
            post.name,
            post.description])
    return response
