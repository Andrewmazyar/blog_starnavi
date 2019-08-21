from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    )
from django.urls import reverse
from .models import Article
from .forms import ArticleForm
from account.models import Profile
from .mixins import FormMessageMixin
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.shortcuts import redirect


class IndexView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Article.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['page_title'] = 'All titles'
        return context


class ArticleCreateView(FormMessageMixin, CreateView):
    model = Article
    template_name = 'post/create.html'
    form_class = ArticleForm
    form_valid_message = 'Article created successfully!'

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.author = profile
        return super(ArticleCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'post/detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        return context

    def add_like(request, article_id):
        try:
            if article_id in request.COOKIES:
                article = Article.objects.get(id=article_id)
                article.like += 1
                article.save()
                response = redirect('/')
                response.set_cookie(article_id, 'navi')
                return response
        except ObjectDoesNotExist:
            raise Http404
        return redirect('/')

    def add_unlike(request, article_id):
        try:
            if article_id in request.COOKIES:
                article = Article.objects.get(id=article_id)
                article.unlike += 1
                article.save()
                response = redirect('/')
                response.set_cookie(article_id, 'navy')
                return response
        except ObjectDoesNotExist:
            raise Http404
        return redirect('/')


