from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse

from wiki.models import Page
from wiki.forms import PageForm

class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })







class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        form = PageForm()
        
        return render(request, 'page.html', {
          'page': page,
          'form': form
        })

    def post(self, request,slug):
      form = PageForm(request.POST)
      page = self.get_queryset().get(slug__iexact=slug) 
      if form.is_valid:
        page.title= request.POST['title']
        page.content= request.POST['content']
        page.author = request.user
        
        page.save()
        return HttpResponseRedirect(
            reverse('wiki-details-page', args=[page.slug]))
      # else if form is not valid
      return render(request, 'wiki-details-page', { 'form': form })

 










class PageCreateView(CreateView):
    def get(self, request):
        context = {
          'form': PageForm()
        }
        return render(request, 'create.html', context)

    def post(self, request):
      form = PageForm(request.POST)
      if form.is_valid:
        page = form.save()
        page.save()
        return HttpResponseRedirect(
          reverse('wiki-details-page', args=[page.slug]))
        
      return render(request, 'create.html', { 'form': form })



