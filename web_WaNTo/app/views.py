from django.shortcuts import render, redirect, get_object_or_404

from .forms import WantoitemForm
from .models import Wantoitem, Main, Except

# chrome関数
from . import def_chrome 



def index(request):
    items = Wantoitem.objects.all()
    # for item in items:
    #     url_dict,except_url_dict = item.scraping()
    #     for url,title in url_dict.items():
    #         item.main_set.create(main_url=url,main_title=title)
    #     for except_url,except_title in except_url_dict.items():
    #         item.except_set.create(except_url=except_url,except_title=except_title)              
    return render(request, 'app/index.html', {
         'items':items,      
        })
    
def detail(request, pk):
    item = get_object_or_404(Wantoitem,pk=pk)
    main_lists = Main.objects.filter(wantoitem=item)
    except_lists = Except.objects.filter(wantoitem=item)
    return render(request, 'app/detail.html', {
         'item':item,
         'main_lists':main_lists,
         'except_lists':except_lists
         })

def form(request):
    if request.method == 'POST':
        form = WantoitemForm(request.POST)
        if form.is_valid():
            form.save()
            new_item = Wantoitem.objects.all().latest('id')
            url_dict,except_url_dict = new_item.scraping()
            for url,title in url_dict.items():
                Main.objects.create(wantoitem=new_item,main_url=url,main_title=title)
            for except_url,except_title in except_url_dict.items():
                Except.objects.create(wantoitem=new_item,except_url=except_url,except_title=except_title)
        return redirect('app:index')
    else:
        form = WantoitemForm()
        return render(request, 'app/form.html',{'form':form})

def delete(request): 
    if request.method == 'POST':    
        item_pks = request.POST.getlist('delete') 
        Wantoitem.objects.filter(pk__in=item_pks).delete()
        return redirect('app:index')
    else:
        items = Wantoitem.objects.all()
        return render(request, 'app/delete.html', {'items':items})

def reload(request, pk):
    if request.method == 'POST':
        item = get_object_or_404(Wantoitem,pk=pk)
        Main.objects.filter(wantoitem=item).delete()
        Except.objects.filter(wantoitem=item).delete()
        url_dict,except_url_dict = item.scraping()
        for url,title in url_dict.items():
            Main.objects.create(wantoitem=item,main_url=url,main_title=title)
        for except_url,except_title in except_url_dict.items():
            Except.objects.create(wantoitem=item,except_url=except_url,except_title=except_title)
        return redirect('app:detail', pk=pk)
    else:
        return redirect('app:detail', pk=pk)