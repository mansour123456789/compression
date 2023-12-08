from django.urls import path 
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index', TemplateView.as_view(template_name='mansour.html'),name='index'),
    path('add-psycopy/', views.addProduct, name="add-prod"), 
    path('add-normal/', views.addProductnormal, name="add-normal"), 
    path('get-normal/', views.getProductnormal, name="get-normal"),
    path('get-psycopy/', views.getProductpsycopy, name="get-psycopy"), 
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
