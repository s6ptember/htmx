from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('table/', views.catalog_table, name='catalog_table'),
    path('srch/', views.search, name='search'),
    path('search-results/', views.search_results, name='search_results'),
    path('modal/', views.modal, name='modal'),
    path('modal/<int:product_id>/', views.modal_content, name='modal_content'),
    path('close-modal/', views.close_modal, name='close_modal'),
]
