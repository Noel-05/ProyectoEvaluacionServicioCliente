from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.conf.urls.static import static 
 
app_name = 'evaluacionCliente'

urlpatterns = [
    
    # URL de base 
    path('', login_required(index)),
    path('evaluacionCliente/index/', login_required(index), name='index'),

]