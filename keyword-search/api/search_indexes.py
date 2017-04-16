# coding=utf-8

from haystack import indexes
from .models import SensitiveWord, FilterWord
from celery_haystack.indexes import CelerySearchIndex


class SensitiveWordIndex(CelerySearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='name')

    def get_model(self):
        return SensitiveWord

class FilterWordIndex(CelerySearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='name')

    def get_model(self):
        return FilterWord
