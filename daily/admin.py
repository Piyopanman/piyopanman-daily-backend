from django.contrib import admin
from .models import Daily, Evaluation, Contact
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
# admin.site.register(Daily)
admin.site.register(Evaluation)
admin.site.register(Daily, MarkdownxModelAdmin)
admin.site.register(Contact)
