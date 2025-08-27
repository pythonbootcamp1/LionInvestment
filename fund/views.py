from django.shortcuts import redirect, render
from .models import Item
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return render(request,'fund/index.html')

def fund_list(request):
    # 펀드 아이템 정보 가져오기
    items = Item.objects.all()
    # context에 담아서 보내기
    context = {
        'items':items
    }
    return render(request,'fund/fund_list.html',context)

from .forms import ItemModelForm
def fund_create(request):
    # # get으로 요청이 오면, 이거는 주소로 접근하는 거라서, 입력 폼을 보여줍니다
    # if request.method=='GET':
    #     return render(request,'fund/fund_create.html')

    # # post로 요청이 오면, DB에 입력하는 요청임으로, DB입력 처리를 끝내고, 다른 페이지를 보여줍니다.
    # elif request.method=='POST':
    #     name_form = request.POST['name']
    #     description_form = request.POST['description']
    #     Item.objects.create(name=name_form, description=description_form)
    #     return redirect('fund:fund_list')
    if request.method=="POST":
        # 받아온 데이터를 처리(저장)
        form = ItemModelForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('fund:fund_list')
    else:
        # 기본 폼을 템플릿에 전달
        form = ItemModelForm()
        context = {
            'form':form
        }
        return render(request,'fund/fund_create.html', context)
        
def fund_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item':item
    }
    return render(request,'fund/fund_detail.html',context)

def fund_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method=="POST":
        form = ItemModelForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            # return redirect('fund:fund_list')
            return redirect('fund:fund_detail', pk=pk)
    else:
        form = ItemModelForm(instance=item)
        context = {
            'form':form
        }
        return render(request,'fund/fund_update.html',context)

def fund_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method=="POST":
        item.delete()
        return redirect('fund:fund_list')
    else:
        return render(request,'fund/fund_delete.html')
