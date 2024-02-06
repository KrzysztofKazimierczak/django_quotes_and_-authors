from django.shortcuts import render, redirect, get_object_or_404
from .forms import TagForm, QuoteForm, AuthorForm, ScrapperForm
from .models import Tag, Quote, Author, ScrapData
from scrap_with_bs import find_data


def main(request):
    quotes = Quote.objects.select_related('author').all()
    return render(request, 'quotesapp/index.html', {"quotes": quotes})




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


def scraper(request, option):
    url = "http://localhost:8000/"
    data = find_data(url, option)

    scrap_data_object = ScrapData(choice=option, dictionary=data)
    scrap_data_object.save()

    return render(request, 'quotesapp/scraped_data.html', {'scraped_data': data})