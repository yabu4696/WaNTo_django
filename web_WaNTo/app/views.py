from django.shortcuts import render, redirect, get_object_or_404

from .forms import WantoitemForm
from .models import Wantoitem


def index(request):
    items = Wantoitem.objects.all()
    return render(request, 'app/index.html', {'items':items})

def form(request):
    if request.method == 'POST':
        form = WantoitemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        form = WantoitemForm()
    return render(request, 'app/form.html',{'form':form})
