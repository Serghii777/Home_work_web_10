from django.shortcuts import render
from django.core.paginator import Paginator

from .utils import get_mongodb


def main(request, page):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={'quotes': quotes_on_page})
