from django.urls import path
from .views import menu, componentes, contactos, nosotros,registro, login, carrito,audifono1,audifono2,audifono3, audifono4, audifono5

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
    
]
