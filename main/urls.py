from django.urls import path
from main.views import show_main, show_landing_page, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, add_stock_ajax, sub_stock_ajax, get_item_json, add_item_ajax, delete_item_ajax


app_name = 'main'


urlpatterns = [
    path('', show_landing_page, name='show_landing_page'),
    path('main/', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    path('get-items/', get_item_json, name='get_item_json'),
    path('create-ajax/', add_item_ajax, name='create_ajax'),
    path('delete-ajax/', delete_item_ajax, name='delete_ajax'),
    path('add-stock/', add_stock_ajax, name='add_stock'),
    path('sub-stock/', sub_stock_ajax, name='sub_stock'),

    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]