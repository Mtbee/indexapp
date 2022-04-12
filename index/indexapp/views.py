from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Progress, Registration, Foods, SendRequest, ReceiveRequest
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


# 物品サービス依頼(発信)
class SendRequestIndex(ListView):
    model = SendRequest
    context_object_name = "sendrequest"
    ordering = ["-number"]

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class SendRequestDetail(DetailView):
    model = SendRequest

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class SendRequestCreate(CreateView):
    model = SendRequest
    fields = "__all__"
    success_url = reverse_lazy("sendrequest_list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class SendRequestUpdate(UpdateView):
    model = SendRequest
    fields = "__all__"
    success_url = reverse_lazy("sendrequest_list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class SendRequestDelete(DeleteView):
    model = SendRequest
    success_url = reverse_lazy("sendrequest_list")

    def get(self, request, pk):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

def SendRequest_csvdownload(request):
    response = HttpResponse(content_type="text/csv; charset=cp932")
    response['Content-Disposition'] = 'attachment; filename = sendrequest.csv'
    writer = csv.writer(response)
    writer.writerow([
        "No.",
        "依頼先",
        "タイトル",
        "担当者",
        ])
    for post in SendRequest.objects.all():
        writer.writerow([
            post.number,
            post.department,
            post.title,
            post.responder,
            ])
    return response


# 物品サービス依頼(受信)
class ReceiveRequestIndex(ListView):
    model = ReceiveRequest
    context_object_name = "receiverequest"
    ordering = ["-number"]

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class ReceiveRequestDetail(DetailView):
    model = ReceiveRequest

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class ReceiveRequestCreate(CreateView):
    model = ReceiveRequest
    fields = "__all__"
    success_url = reverse_lazy("receiverequest_list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class ReceiveRequestUpdate(UpdateView):
    model = ReceiveRequest
    fields = "__all__"
    success_url = reverse_lazy("receiverequest_list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class ReceiveRequestDelete(DeleteView):
    model = ReceiveRequest
    success_url = reverse_lazy("receiverequest_list")

    def get(self, request, pk):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

def ReceiveRequest_csvdownload(request):
    response = HttpResponse(content_type="text/csv; charset=cp932")
    response['Content-Disposition'] = 'attachment; filename = receiverequest.csv'
    writer = csv.writer(response)
    writer.writerow([
        "No.",
        "依頼元",
        "タイトル",
        "担当者",
        ])
    for post in ReceiveRequest.objects.all():
        writer.writerow([
            post.number,
            post.department,
            post.title,
            post.responder,
            ])
    return response