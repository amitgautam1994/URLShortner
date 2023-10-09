from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('create/', createShortURL, name='create'),
    path('<str:url>', redirectPage, name='redirect'),
    # path('login/', LoginView.as_view(), name='login'),
]
