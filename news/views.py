from django.shortcuts import render
from django.views.generic import ListView, DetailView

from news.models import News


class NewsListView(ListView):
    model = News
    template_name = "news/news-list.html"
    context_object_name = "all_news"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news"] = News.published.all().filter(category__name="News")

        return context
    

class NewsDetailView(DetailView):
    model = News
    pk_url_kwarg = 'id'
    template_name = 'news/news-detail.html'
    context_object_name = 'news'

