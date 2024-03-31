from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .utils import get_mongodb
from .models import Author, Quote
from .forms import AuthorForm, QuoteForm
from django.contrib.auth.decorators import login_required
from quotes.templatetags.extract import get_author



def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={'quotes': quotes_on_page})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user  
            author.save()
            return redirect(to='quotes:root')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})
@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.author = Author.objects.get(user=request.user)  
            quote.save()
            form.save_m2m()  
            return redirect(to='quotes:root') 
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

def author_detail(request, author_id):
    author = get_author(author_id)
    return render(request, 'quotes/author_detail.html', {'author': author})