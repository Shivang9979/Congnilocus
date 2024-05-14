from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('quiz/', views.get_questions, name='get_questions'),
    path('user_input/', views.process_user_input,
         name='user_input'),  # type: ignore

]
