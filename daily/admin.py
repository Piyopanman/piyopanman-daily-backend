from django.contrib import admin
from .models import Daily, Evaluation, Contact
from markdownx.admin import MarkdownxModelAdmin


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'twitter', 'oshi', 'datetime',)


admin.site.register(Evaluation)
admin.site.register(Daily, MarkdownxModelAdmin)
admin.site.register(Contact, ContactAdmin)
