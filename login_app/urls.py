
from django.urls import path,include
from  login_app.views import sgin_up,sgin_in

urlpatterns = [
  
    path('reg',sgin_up),
     path('log',sgin_in)
]


