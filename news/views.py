from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views import View
from django.core.paginator import Paginator

from news.models import News


# class NewsListView(ListView):
#     model = News
#     template_name = "news/news-list.html"
#     context_object_name = "all_news"    

#     def get(self, request):
#         news = News.published.all().filter(category__name="News").order_by('id')
#         search_query = request.GET.get('q', '')
#         if search_query:
#             news = news.filter(title__icontains=search_query)

#         context = {
#             "news": news,
#             "search_query": search_query,
#         }

#         return render(request, "news/news-list.html", context)
    

class NewsListView(View):
    def get(self, request):
        news = News.published.all().filter(category__name="News").order_by('id')
        search_query = request.GET.get('q', '')
        if search_query:
            news = news.filter(title__icontains=search_query)

        page_size = request.GET.get('page_size', 6)
        paginator = Paginator(news, page_size)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        context = {
            "page_obj": page_obj,
            "search_query": search_query,
        }

        return render(request, 'news/news-list.html', context)


class NewsDetailView(DetailView):
    model = News
    pk_url_kwarg = 'id'
    template_name = 'news/news-detail.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_news"] = (
            News.published.all()
            .order_by("-published_time")
            .filter(category__name="News")[:5]
        )

        return context
