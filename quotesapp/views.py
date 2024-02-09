from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import TagForm, QuoteForm, AuthorForm
from .models import Tag, Quote, Author, ScrapData
from scrap_with_bs import find_data
import subprocess, os, json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def main(request):
    quotes_list = Quote.objects.select_related('author').all()
    paginator = Paginator(quotes_list, 2)
    page_number = request.GET.get('page')
    try:
        quotes = paginator.page(page_number)
    except PageNotAnInteger:
        quotes = paginator.page(1)
    except EmptyPage:
        quotes = paginator.page(paginator.num_pages)

    top_tags = Tag.objects.annotate(num_quotes=Count('quote')).filter(num_quotes__gt=0).order_by('-num_quotes')[:10]
    return render(request, 'quotesapp/index.html', {'quotes': quotes, 'top_tags': top_tags, 'page_obj': quotes})





def quote(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'quotesapp/quote.html', {"quote": quote})

def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotesapp/author.html', {"author": author})

def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/add_tag.html', {'form': form})

    return render(request, 'quotesapp/add_tag.html', {'form': TagForm()})

def add_quote(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_tags = Tag.objects.filter(tag__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/add_quote.html', {"tags": tags, 'form': form})

    return render(request, 'quotesapp/add_quote.html', {"tags": tags, 'form': QuoteForm()})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/add_author.html', {'form': form})

    return render(request, 'quotesapp/add_author.html', {'form': AuthorForm()})

def delete_quote(request, quote_id):
    Quote.objects.get(pk=quote_id).delete()
    return redirect(to='quotesapp:main')

def quotes_by_tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    quotes = Quote.objects.filter(tags=tag)
    return render(request, 'quotesapp/quotes_by_tag.html', {'tag': tag, 'quotes': quotes})

def top_ten_tags(request):
    quotes = Quote.objects.all()
    tag_counts = Tag.objects.annotate(num_quotes=Count('quote')).filter(num_quotes__gt=0).order_by('-num_quotes')[:10]
    
    context = {
        'quotes': quotes,
        'top_tags': tag_counts,
    }
    return render(request, 'quotesapp/top_ten_tags.html', context)



# Beautifoul soup scraper

def scraper(request, option):
    url = "http://localhost:8000/"
    data = find_data(url, option)

    scrap_data_object = ScrapData(choice=option, dictionary=data)
    scrap_data_object.save()

    return render(request, 'quotesapp/scraped_data.html', {'scraped_data': data})



# Scrapy scraper
"""
def scraper(request, option):
    django_project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    scrapy_project_dir = os.path.join(django_project_dir, 'scrapmyside/scrapmyside')
    os.chdir(scrapy_project_dir)
    
    process = subprocess.Popen(['scrapy', 'crawl', 'myspider', '-a', f'data_to_scrap={option}'], stdout=subprocess.PIPE)
    output, _ = process.communicate()

    while output:
        break

    os.chdir(django_project_dir)

    latest_scrap_data = ScrapData.objects.latest('id')
    data_to_show = latest_scrap_data.dictionary

    return render(request, 'quotesapp/scraped_data.html', {'scraped_data': data_to_show})
"""