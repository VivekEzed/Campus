from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('',views.login_,name="renderloginpage"),
    path('home/',views.homepage,name="adminhomepage"),
    path('members/',views.load_memberspage,name="members"),
    path('addmembers/',views.addmembers,name="addmembers"),
    path('login/',views.loginpage,name="login"),
    path('membersinfo/<int:id>/',views.membersfullinfo,name="membersinfo"),
    path('offers/',views.load_offerspage,name="offers"),
    path('addoffers/',views.add_offers,name="addoffers"),
    path('posts/',views.load_postpage,name="posts"),
    path('addposts/',views.add_postspage,name="addposts"),
    path('points/',views.load_pointspage,name="points"),
    path('addpoints/',views.load_addpointspage,name="addpoints"),
    path('logout/',views.logout_view,name="logout"),
    path('load',views.load,name="load"),
    
] 