from django.shortcuts import render
from django.views.generic import ListView,DetailView
from bookmark.models import Bookmark


# 전체의 question
class BookmarkLV(ListView):
    model = Bookmark

    
    # template_name =  "bookmark/bookmark_list.html" #appname/mode_name_list.html
    # context_object_name = "object_list" #object_list 

# 몇 번째 question인지가 중요
class BookmarkDV(DetailView):
    model = Bookmark
    # template_name = 'bookmark/bookmark_detail.html'
    # context_object_name = 'bookmark'
