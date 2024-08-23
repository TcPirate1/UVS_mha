from django.contrib import admin
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.urls import path
from .models import Card

# Register your models here.
class CardAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('add_card/', self.admin_site.admin_view(self.add_card_view))
        ]
        return custom_urls + urls

    def add_card_view(self, request):
        context = dict(
            self.admin_site.each_context(request),
            key = "value"
        )
        return TemplateResponse(request, "add_card.html", context)

admin.site.register(Card, CardAdmin)