from django.urls import path
from API import views 


urlpatterns = [
    path('', views.AllMethods, name='allmethods'),
    path('search-lyrics/<str:q>', views.Lyrics, name='lyrics')
]