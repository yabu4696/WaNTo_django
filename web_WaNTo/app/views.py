from django.shortcuts import render, redirect, get_object_or_404

# from .forms import UphtmlForm, SubjectForm
# from .models import Subject, Uphtml


def index(request):
    return render(request, 'app/index.html')
