# coding=utf-8

from django.http import JsonResponse
from haystack.query import SearchQuerySet
from django.views.generic import View
import jieba
from .forms import SearchForm


class ApiSearch(View):
    def get(self, request, *args, **kwargs):
        form = SearchForm(request.GET)
        if not form.is_valid():
            ret = dict(status=False)
            return JsonResponse(ret)

        data = form.cleaned_data
        text = data['text']
        words = jieba.lcut(text.strip(), cut_all=False)
        keywords = list()

        for word in words:
            result_count = SearchQuerySet().filter(text=word).count()
            if result_count > 0:
                keywords.append(word)

        ret = dict(status=True, text=text, keywords=keywords)
        return JsonResponse(ret)
