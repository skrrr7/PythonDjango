from django.urls import path
from .views import home_view, login_view, signup_view 

urlpatterns = [
    path('', home_view, name='home'),  # Home page
    path('login/', login_view, name='login'),  # Login page
    path('signup/', signup_view, name='signup'),  # Signup page
]
