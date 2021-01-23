from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.db.models import Q
from .models import*
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
    post = Article.objects.all().order_by('-date')
    liste = Article.objects.all().order_by('date')
    paginator = Paginator(post, 4)
    page_number = request.GET.get('page')
    
    try:
        page_object = paginator.page(page_number)
    except PageNotAnInteger:
        page_object = paginator.page(1)
    except EmptyPage:
        page_object = paginator.page(paginator.num_pages)

    paginator0 = Paginator(liste, 3)
    page_number0 = request.GET.get('page')

    try:
        page_object0 = paginator0.page(page_number)
    except PageNotAnInteger:
        page_object0 = paginator0.page(1)
    except EmptyPage:
        page_object0 = paginator0.page(paginator0.num_pages)
    return render(request, 'blog/index.html', {'page_obj': page_object,'liste':page_object0})


def detail(request, pk):
    post = get_object_or_404(Article, pk=pk)
    content = {"box": post}
    return render(request, 'blog/detail.html', content)


def search(request):
    searching = request.GET.get('query')
    article = Article.objects.filter(Q(title__contains=searching) | Q(
        description__contains=searching) | Q(paragraphe0__contains=searching) | Q(paragraphe1__contains=searching) | Q(paragraphe2__contains=searching) | Q(url0__contains=searching) | Q(url1__contains=searching) | Q(url2__contains=searching) | Q(url3__contains=searching) | Q(auteur__contains=searching))
    content = {'article': article}
    return render(request, 'blog/search.html', content)


def blog(request):
    blog = Article.objects.all()
    paginator = Paginator(blog, 4)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:

        posts = paginator.page(1)
    except EmptyPage:

        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog.html', {'page': page, 'posts': posts})
