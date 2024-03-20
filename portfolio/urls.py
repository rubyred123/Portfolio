from django.urls import path
from portfolio import views

urlpatterns= [
    path('',views.index, name="index"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('resume',views.resume, name="resume"),
    path('blog',views.blog, name="blog"),
]