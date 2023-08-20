from django.contrib import admin
from django.urls import path
from datainput.views import home,data_input

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('data-input/', data_input, name='data_input'),
]
