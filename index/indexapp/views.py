from re import template
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import ProgressNB, ProgressPB, Registration, Foods, Foods46, SendRequest, ReceiveRequest, Roulette
from django.http import HttpResponse
import csv, random
from django.contrib.auth.decorators import login_required

@login_required
def top(request):
    return render(request, 'top.html')

# 制作進行NB
class ProgressNBIndex(ListView):
    model = ProgressNB
    context_object_name = "progressnb"
    ordering = ["-number"]

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class ProgressNBDetail(DetailView):
    model = ProgressNB

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class ProgressNBCreate(CreateView):
    model = ProgressNB
    fields = "__all__"
    success_url = reverse_lazy("progressnb_list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class ProgressNBUpdate(UpdateView):
    model = ProgressNB
    fields = "__all__"
    success_url = reverse_lazy("progressnb_list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class ProgressNBDelete(DeleteView):
    model = ProgressNB
    success_url = reverse_lazy("progressnb_list")

    def get(self, request, pk):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

def ProgressNB_csvdownload(request):
    response = HttpResponse(content_type="text/csv; charset=cp932")
    response['Content-Disposition'] = 'attachment; filename = progressnb_index.csv'
    writer = csv.writer(response)
    writer.writerow([
        "No.",
        "コード",
        "品名",
        "登録日",
        "更新日"
    ])
    for post in ProgressNB.objects.all():
        writer.writerow([
            post.number,
            post.code,
            post.name,
            post.created_at.strftime("%Y/%m/%d"),
            post.updated_at.strftime("%Y/%m/%d")])
    return response




# 制作進行PB
class ProgressPBIndex(ListView):
    model = ProgressPB
    context_object_name = "progresspb"
    ordering = ["-number"]

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class ProgressPBDetail(DetailView):
    model = ProgressPB

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class ProgressPBCreate(CreateView):
    model = ProgressPB
    fields = "__all__"
    success_url = reverse_lazy("progresspb_list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class ProgressPBUpdate(UpdateView):
    model = ProgressPB
    fields = "__all__"
    success_url = reverse_lazy("progresspb_list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class ProgressPBDelete(DeleteView):
    model = ProgressPB
    success_url = reverse_lazy("progresspb_list")

    def get(self, request, pk):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

def ProgressPB_csvdownload(request):
    response = HttpResponse(content_type="text/csv; charset=cp932")
    response['Content-Disposition'] = 'attachment; filename = progresspb_index.csv'
    writer = csv.writer(response)
    writer.writerow([
        "No.",
        "コード",
        "品名",
        "登録日",
        "更新日"
    ])
    for post in ProgressPB.objects.all():
        writer.writerow([
            post.number,
            post.code,
            post.name,
            post.created_at.strftime("%Y/%m/%d"),
            post.updated_at.strftime("%Y/%m/%d")])
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
        "リスト更新",
        "登録日",
        "更新日"    
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
            post.update,
            post.created_at.strftime("%Y/%m/%d"),
            post.updated_at.strftime("%Y/%m/%d")
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
        "リスト更新",
        "登録日",
        "更新日"  
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
            post.update,
            post.created_at.strftime("%Y/%m/%d"),
            post.updated_at.strftime("%Y/%m/%d")
            ])
    return response


# TF46期原料登録
class Foods46Index(ListView):
    model = Foods46
    context_object_name = "foods46"
    ordering = ["-number"]

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class Foods46Detail(DetailView):
    model = Foods46

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class Foods46Create(CreateView):
    model = Foods46
    fields = "__all__"
    success_url = reverse_lazy("foods46_list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class Foods46Update(UpdateView):
    model = Foods46
    fields = "__all__"
    success_url = reverse_lazy("foods46_list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class Foods46Delete(DeleteView):
    model = Foods46
    success_url = reverse_lazy("foods46_list")

    def get(self, request, pk):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

def Foods46_csvdownload(request):
    response = HttpResponse(content_type="text/csv; charset=cp932")
    response['Content-Disposition'] = 'attachment; filename = TF46_registration_index.csv'
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
        "リスト更新",
        "登録日",
        "更新日"  
    ])
    for post in Foods46.objects.all():
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
            post.update,
            post.created_at.strftime("%Y/%m/%d"),
            post.updated_at.strftime("%Y/%m/%d")
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
        "登録日",
        "更新日"
        ])
    for post in SendRequest.objects.all():
        writer.writerow([
            post.number,
            post.department,
            post.title,
            post.responder,
            post.created_at.strftime("%Y/%m/%d"),
            post.updated_at.strftime("%Y/%m/%d")
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
        "登録日",
        "更新日"
        ])
    for post in ReceiveRequest.objects.all():
        writer.writerow([
            post.number,
            post.department,
            post.title,
            post.responder,
            post.created_at.strftime("%Y/%m/%d"),
            post.updated_at.strftime("%Y/%m/%d")
            ])
    return response

    # ルーレット
class RouletteIndex(ListView):
    queryset = Roulette.objects.order_by('?')[:20]
    context_object_name = "roulette_ex"
    template_name = "roulette_list.html"

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class RouletteDelete(DeleteView):
    model = Roulette
    success_url = reverse_lazy("roulette_list")

    def get(self, request, pk):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

class RouletteCreate(CreateView):
    model = Roulette
    fields = "__all__"
    success_url = reverse_lazy("roulette_list")

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().get(request)

    
    #パッカー
def index(request) :
    if not request.user.is_active:
        return redirect('/accounts/login/?next=%s' % request.path)
    return render(request, "packers/index.html")