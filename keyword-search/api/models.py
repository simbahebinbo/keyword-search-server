# coding=utf-8

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categorys')

    def __str__(self):
        return self.name

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

admin.site.register(Category, CategoryAdmin)

class SensitiveWord(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _('sensitiveword')
        verbose_name_plural = _('sensitivewords')

    def __str__(self):
        return self.name


class SensitiveWordAdmin(admin.ModelAdmin):
    list_display = ('category', 'name')
    search_fields = ('category', 'name')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)


admin.site.register(SensitiveWord, SensitiveWordAdmin)

class FilterWord(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _('filterword')
        verbose_name_plural = _('filterwords')

    def __str__(self):
        return self.name

class FilterWordAdmin(admin.ModelAdmin):
    list_display = ('category', 'name')
    search_fields = ('category', 'name')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

admin.site.register(FilterWord, FilterWordAdmin)


