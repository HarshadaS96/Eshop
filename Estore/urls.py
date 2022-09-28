from django.contrib import admin
from django.urls import path,include
from .views import Index, Cart, Login
from . import views

app_name = 'Estore'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', Index.as_view(), name='homepage'),
    path('signup/', views.signup),
    path('login/', Login.as_view()),
    path('cart/', Cart.as_view()),
    path('logout/', views.logout, )
]