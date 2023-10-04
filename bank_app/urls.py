from django.urls import path
from .views import *


urlpatterns=[
    path('index/',index),
    path('Register/',Register),
    path('Login/',Login),
    path('profile/',profile),
    path('edit/<int:id>',edit),
    path('editimage/',editimage),
    path('addamount/<int:id>',addamount),
    path('success/',success),
    path('amountwithdraw/<int:id>',amountwithdraw),
    path('withdraw/',withdraw),
    path('checkbal/',checkbal),
    path('checkbal1/',checkbal1),
    path('ministatement/<int:id>',ministatement),
    path('depositstatement/',depositstatement),
    path('withdrawstatement/',withdrawstatement),
    path('newsupload/',newsupload),
    path('adminlogin/',adminlogin),
    path('alog/',alog),
    path('newsdisplay/',newsdisplay),
    path('newsedit/<int:id>',newsedit),
    path('newsdelete/<int:id>',newsdelete),
    path('usernewsdisplay/',usernewsdisplay),
    path('wish/<int:id>',wish),
    path('wishdisplay/',wishdisplay),
    path('wish_rem/<int:id>',wish_rem),
    path('logout/',logout_view),
    path('forgot/',forgot_password),
    path('change/<int:id>',change_password),
    path('moneytransfer/<int:id>',moneytransfer)



]