from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.logininfo,name="login"),
    path('register',views.registeration,name="register"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout',views.logout,name = "logout"),
    path('fruits',views.fruits,name="fruits"),
    path('tubers',views.tubers,name="tubers"),
    path('vegs',views.vegs,name="vegs"),
    path('greens',views.greens,name="greens"),
    path('fruitsdetails/<str:name>/',views.viewfruits,name="fruitsdetails"),
    path('tubersdetails/<str:name>/',views.viewtubers,name="tubersdetails"),
    path('vegsdetails/<str:name>/',views.viewvegs,name="vegsdetails"),
    path('greensdetails/<str:name>/',views.viewgreens,name="greensdetails"),
    path('profile',views.profile,name='profile'),
    path('update/<int:id>',views.nav,name='update'),
    path('viewdetail/<str:name>/',views.viewdetail,name = "viewdetail")
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)