from django.contrib import admin
from board.models import Board, Food, Comment
# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    search_fields =  ['title']
    list_display = ['id','title', 'category','created_at']
    list_display_links = ['title']
    list_filter=['created_at']
    prepopulated_fields = {'slug':('title',),}

admin.site.register(Board,BoardAdmin)
admin.site.register(Comment)
admin.site.register(Food)