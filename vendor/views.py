from django.shortcuts import render
from .models import Vendor
from .forms import VendorForm # 要記得 import 相對應的 Model Form 唷!
from .forms import RawVendorForm # 新增 RawVendorForm
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView
from django import forms
# Create your views here.
#def showtemplate(request):
#    # 今天先不探討什麼是 render，先記得它會去撈 test.html
#    return render(request, 'test.html')
# 對應 views 的 showtemplate
def showtemplate(request):
    vendor_list = Vendor.objects.all()
    context = {'vendor_list': vendor_list}
    # print(vendor_list)
    return render(request, 'vendors/detail.html', context)
    
def vendor_index(request):
    vendor_list = Vendor.objects.all() # 把所有 Vendor 的資料取出來
    context = {'vendor_list': vendor_list} # 建立 Dict對應到Vendor的資料，
    return render(request, 'vendors/vendor_detail.html', context)
    
def singleVendor(request, id):
    vendor_list = get_object_or_404(Vendor, id=id)
    # try:
    #     vendor_list = Vendor.objects.get(id=id)
    # except Vendor.DoesNotExist:
    #     raise Http404
    context = {
        'vendor_list': vendor_list
    }
    return render(request, 'vendors/vendor_detail.html', context)
'''
# 針對 vendor_create.html
def vendor_create_view(request):
    form = VendorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = VendorForm()#Clear form
    context = {
        'form' : form
    }
    return render(request, "vendors/vendor_create.html", context)
    
'''
'''
def vendor_create_view(request):
    form = RawVendorForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = VendorForm()
    context = {
        'form' : form
    }
    return render(request, "vendors/vendor_create.html", context)
'''
def vendor_create_view(request):
    form = RawVendorForm(request.POST or None)
    if form.is_valid():
        Vendor.objects.create(**form.cleaned_data) # 新增
        form = RawVendorForm()
    context = {
        'form' : form
    }
    return render(request, "vendors/vendor_create.html", context)



class VendorListView(ListView):
    model = Vendor
    template_name = 'vendor/vendor_lst.html'

# 繼承 DetailView
class VendorDetailView(DetailView):
    model = Vendor
    # queryset = Vendor.objects.all()
    template_name = 'vendor/vendor_detail.html'

class VendorCreateView(CreateView):
    # form_class = VendorModelForm
    model = Vendor
    fields='__all__'
    #fields= ['vendor_name', 'store_name']
    template_name = 'vendor/vendor_create.html'

class VendorModelForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
            # fields = (
            #         'vendor_name',
            #         'store_name',
            #         'phone_number',
            #         'address',
            # )
        labels = {
            'vendor_name': ('攤販名稱'),
            'store_name' : ('店名'),
            'phone_number' : ('電話'),
            'address' : ('地址'),
        }
    
# CreateView
class VendorCreateView(CreateView):
    form_class = VendorModelForm
    # model = Vendor
    # fields= ['vendor_name', 'store_name']
    template_name = 'vendors/vendor_create.html'

class VendorUpdateView(UpdateView):
    form_class = VendorModelForm
    template_name = 'vendors/vendor_create.html'
    queryset = Vendor.objects.all() # 這很重要
    

