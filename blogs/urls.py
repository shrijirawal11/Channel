from django.urls import path
from .views import home, aboutus, testinomals,contact,blogs,authors,login, register, landing


urlpatterns = [
    path('', home, name='home'),
    path('aboutus', aboutus, name='aboutus'),
    path('testinomals',testinomals, name='testinomals'),
    path('contact',contact, name='contact'),
    path('blogs',blogs, name='blogs'),
    path('authours',authors, name='authors'),
    path('login',login, name='login'),
    path('register',register, name='register'),
    path('main', landing, name="landingPage")
]
