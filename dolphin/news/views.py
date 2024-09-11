from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def news_page(request):
    return render(request, 'news/news.html', context={'page_title': 'Новости'})
