from django.conf.urls import url
from .import views
from django.views.generic import RedirectView

app_name='productapp'

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^productapp/',RedirectView.as_view(pattern_name='productapp:index',permanent=True)),
    url(r'^product/list/',views.product_list,name='prolist'),
    url(r'^prolist/$',views.pro_list,name='mylist'),
    url(r'^mycarts/$',views.mycart, name='mycart-selection'),
    url(r'^cart/add/(?P<pk>\d+)/', views.cart_add, name='cart_add'),
    url(r'^cart/cart_clear/', views.cart_clear, name='cart_clear'),
    
]
