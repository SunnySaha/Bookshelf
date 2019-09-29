from django.shortcuts import render
from django.http import HttpResponse, request
from .models import BookList
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


class BooklistView(ListView, LoginRequiredMixin):

        model = BookList
        template_name = 'pdflist/home.html'
        context_object_name = 'items'
        ordering = ['-date_upload']


def about(request):
    return render(request, 'pdflist/about.html')