from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    # path('login/', LoginView.as_view(), name='login'),
]
