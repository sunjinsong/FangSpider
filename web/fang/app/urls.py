from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
        #path('city/<int:id>/',views.city),
    path('area/<int:city_id>/<int:area_id>/<int:page_num>/',views.area),
    path('tu/',views.tu),
    path('deal/',views.deal),
]
