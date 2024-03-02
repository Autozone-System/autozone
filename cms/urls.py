from django.urls import path, include
from . import views




urlpatterns = [
    path('', 'cms.views.HomeController', name='dashboard'),
    path('admin', include('auth.urls')),
    path('unit', include('cms.views.UnitController')),
    path('tag', include('cms.views.TagsController')),
]
