
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ReactView.as_view()),
    path('account-verified',account_verified.as_view()),
    path('signin',SIGNIN.as_view()),
    path('showuser',GETUSER.as_view()),
    path('showscore',GETSCORE.as_view()),
    path('showtask',GETTASK.as_view()),
    path('forgotpassword',Forgotpassword.as_view()),
]
