from django.shortcuts import render
from .models import BookList
from django.contrib import messages
from django.views.generic import (ListView,
                                  CreateView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView,
                                  )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User



class BooklistView( LoginRequiredMixin,ListView):
        model = BookList
        template_name = 'pdflist/home.html'
        context_object_name = 'items'
        ordering = ['-date_upload']
        paginate_by = 6


class UserpostListview(LoginRequiredMixin,ListView):
    model =BookList
    template_name = 'pdflist/user_post.html'
    context_object_name = 'items'
    paginate_by = 6


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return BookList.objects.filter(user=user).order_by('-date_upload')


class bookCreateView(LoginRequiredMixin, CreateView):
    model = BookList
    fields = ['title', 'author', 'pdf_file','make_public']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class postUpdateView(LoginRequiredMixin,UpdateView):
    model = BookList
    fields = ['title', 'author', 'pdf_file', 'make_public']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class postDeleteview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BookList
    success_url = '/'

    def test_func(self):
        items = self.get_object()
        if self.request.user == items.user:
            return True
        return False

def about(request):
    return render(request, 'pdflist/about.html')

def Contacts(request):
    return render(request, 'pdflist/contact.html')