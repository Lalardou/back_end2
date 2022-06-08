from django.urls import path
from .views import menu, componentes, contactos, monitor1, nosotros,registro, login, carrito,audifono1,audifono2,audifono3, audifono4, audifono5
from .views import monitor1,monitor2,monitor3,monitor4,monitor5,componenteM

urlpatterns = [
    path('',menu,name='menu'),
    path('componentes',componentes,name='componentes'),
    path('contactos/',contactos,name='contactos'),
    path('nosotros/',nosotros,name='nosotros'),
    path('registro/',registro,name='registro'),
    path('login/',login,name='login'),
    path('carrito/',carrito,name='carrito'),
    path('audifono1/',audifono1, name='audifono1'),
    path('audifono2/',audifono2, name='audifono2'),
    path('audifono3/',audifono3, name='audifono3'),
    path('audifono4/',audifono4, name='audifono4'),
    path('audifono5/',audifono5, name='audifono5'),
    path('monitor1/',monitor1, name='monitor1'),
    path('monitor2/',monitor2, name='monitor2'),
    path('monitor3/',monitor3, name='monitor3'),
    path('monitor4/',monitor4, name='monitor4'),
    path('monitor5/',monitor5, name='monitor5'),
    path('componenteM/',componenteM, name='componenteM'),
]
