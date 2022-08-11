from django.urls import path
from .views import *

urlpatterns = [
#    path('', index, name='home'),
    path('', HomePage, name = 'home'),
    path('about', about),
    path('create', create),
    path('order/<int:tovar_id>', order, name='order'),
    path('category/<int:category_id>/', TovarByCat.as_view(), name='category'),
    path('tovar/<int:tovar_id>/', tovar_page, name='tovar'),
#    path('tovar/<int:pk>/', TovarPage.as_view(), name='tovar'),
#    path('packet', Packet.as_view(), name='Packet'),
    path('packet', user_Packet, name='Packet'),
    path('registrate', register, name='registrate'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout')
]
