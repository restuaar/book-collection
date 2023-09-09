from django.urls import path
from main.views import show_main, show_landing_page

app_name = 'main'

urlpatterns = [
    path('main/', show_main, name='show_main'),
    path('', show_landing_page, name='show_landing_page'),
]