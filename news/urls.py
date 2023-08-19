from django.urls import path

from news.views import NewsListView, NewsDetailView

app_name = "news"
urlpatterns = [
    path('', NewsListView.as_view(), name="news_list"),
    path('detail/<int:id>/', NewsDetailView.as_view(), name="news_detail"),
]