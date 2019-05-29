from django.urls import path
from .import views


from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('',views.user_homepage,name="userhomepage"),
    path('offers/',views.load_offerspage,name="user_offers"),
    path('posts/',views.load_postspage,name="user_posts"),
    path('points/',views.load_pointstspage,name="user_points"),
    path('profile/',views.load_yourprofile,name="user_profile"),
    
    
] 