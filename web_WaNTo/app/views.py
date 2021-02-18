from django.shortcuts import render, redirect, get_object_or_404

from .forms import WantoitemForm
from .models import Wantoitem

# chrome関数
from . import def_chrome 



def index(request):
    items = Wantoitem.objects.all()
    return render(request, 'app/index.html', {'items':items})
    
def detail(request, pk):
    item = get_object_or_404(Wantoitem,pk=pk)
    
    driver = def_chrome.make_driver()
    driver.get("https://google.com")
    def_chrome.search(driver,item.item_name)

    except_file = '/workspace/app/except_list.txt'
    page_range = 3

    url_list,except_url_list = def_chrome.get_url(driver,page_range,except_file)
    driver.close()

    return render(request, 'app/detail.html', {
         'item':item,
         'url_list':url_list, 
         'except_url_list':except_url_list
         })

def form(request):
    if request.method == 'POST':
        form = WantoitemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        form = WantoitemForm()
    return render(request, 'app/form.html',{'form':form})
