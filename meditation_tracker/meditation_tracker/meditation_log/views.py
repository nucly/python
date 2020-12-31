from django.shortcuts import render
from django.urls import path
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'meditation_log/index.html'

    def get_queryset(self):
        return {'test'}
