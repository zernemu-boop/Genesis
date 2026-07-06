
from django.contrib import admin
from django.urls import path
from Genesisapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('details/', views.details, name = 'home'),

    path('blog/', views.blog, name = 'blog'),

    path('', views.home, name = 'home'),

    path('portfolio/', views.portfolio, name = 'portfolio'),

    path('service/', views.service, name = 'service'),

    path('starter/', views.starter, name = 'starter'),
    
    path('show/', views.show, name = 'show'),
    
    path('delete/<int:id>', views.delete),
    
    path('edit/<int:id>', views.edit),

]
