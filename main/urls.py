from django.urls import path
from main.views import show_main, show_landing_page, create_book, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, delete_item, add_stock, sub_stock


app_name = 'main'

urlpatterns = [
    path('', show_landing_page, name='show_landing_page'),
    path('main/', show_main, name='show_main'),
    path('tambah_buku/', create_book, name='show_tambah_buku'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete/<int:id>/)', delete_item, name='delete'),
    path('add_stock/<int:id>/', add_stock, name='add_stock'),
    path('sub_stock/<int:id>/', sub_stock, name='sub_stock'),

    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]