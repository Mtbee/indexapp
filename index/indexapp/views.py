from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Progress, Registration, Foods, Estimate
from django.http import HttpResponse
import csv
from django.contrib.auth.decorators import login_required

@login_required
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
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
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
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
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
        "内容",
        "仕入先",
        "備考",
        "依頼書作成",
        "カクテル登録",
        "リスト更新"    
    ])
    for post in Registration.objects.all():
        writer.writerow([
            post.number,
            post.code,
            post.name,
            post.category,
            post.supplier,
            post.description,
            post.writer,
            post.register,
            post.update
            ])
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
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
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
        "内容",
        "仕入先",
        "得意先",
        "備考",
        "依頼書作成",
        "カクテル登録",
        "リスト更新"  
    ])
    for post in Foods.objects.all():
        writer.writerow([
            post.number,
            post.code,
            post.name,
            post.category,
            post.supplier,
            post.cutomer,
            post.description,
            post.writer,
            post.register,
            post.update
            ])
    return response


# 見積依頼
class EstimateIndex(ListView):
    model = Estimate
    context_object_name = "estimate"
    ordering = ["-number"]

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class EstimateDetail(DetailView):
    model = Estimate

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class EstimateCreate(CreateView):
    model = Estimate
    fields = "__all__"
    success_url = reverse_lazy("estimate_list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class EstimateUpdate(UpdateView):
    model = Estimate
    fields = "__all__"
    success_url = reverse_lazy("estimate_list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class EstimateDelete(DeleteView):
    model = Estimate
    success_url = reverse_lazy("estimate_list")

    def get(self, request, pk):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

def Estimate_csvdownload(request):
    response = HttpResponse(content_type="text/csv; charset=cp932")
    response['Content-Disposition'] = 'attachment; filename = estimate.csv'
    writer = csv.writer(response)
    writer.writerow([
        "No.",
        "見積依頼",
        "品名",
        "形態",
        "企画期限",
        "依頼部門",
        "備考",
        "担当者",
        ])
    for post in Estimate.objects.all():
        writer.writerow([
            post.number,
            post.client,
            post.name,
            post.form,
            post.deadline,
            post.requester,
            post.description,
            post.responder,
            ])
    return response
