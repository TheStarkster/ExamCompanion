from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('about/',views.about),
    # path('',views.homepage),
    path('Register/',include('Auth.urls')),
]
