from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Album, Photo


class AlbumLV(ListView):
    model = Album

    # default 값
    # context_object_name = 'object_list', 내가 따로 지정할 수 있음
    
    # ListView의 기본 템플릿 : 앱이름/모델_list.html
    template_name = 'photo/album_list.html'

  
    # def get_queryset(self) -> QuerySet[Any]:
    #     return self.model.object.all()
    
    # detailview에서 사용되는 것
    # def get_object(self)

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     return super().get_context_data(**kwargs)

# 특정 데이터를 가져와야 해서 pk값을 받아요
class AlbumDV(DetailView):
    model = Album
    template_name = 'photo/album_detail.html'
    # pk를 통해서 특정 앨범만 가져옴

class PhotoDV(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'
