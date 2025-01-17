from django.urls import path

from exam.views import my_filter, q_filter, f_filter

app_name = 'exam'

urlpatterns = [
    path('', my_filter, name='list'),
    path('', q_filter, name='list'),
    path('', f_filter, name='list'),
]
