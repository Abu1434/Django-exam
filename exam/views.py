from django.shortcuts import render

from exam.models import SpecialModel, PersonModel

from django.db.models import Q, F


def my_filter(request):
    special_model = SpecialModel.objects.filter(age__gt=25)
    context = {
        'special_model': special_model,
    }
    return render(request, 'index.html', context)


def q_filter(request):
    q_model = SpecialModel.objects.filter(Q(name__startswith='J'))
    context = {
        'q_model': q_model,
    }
    return render(request, 'index.html', context)


def f_filter(request):
    f_model = PersonModel.objects.filter(age__gt=F('birthday'))
    context = {
        'f_model': f_model,
    }
    return render(request, 'index.html', context)
