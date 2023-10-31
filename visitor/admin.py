from django.contrib import admin
from visitor.models import Visitor

# Register your models here.
@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    pass