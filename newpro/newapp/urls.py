from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('home.html/',views.home),
    path('aboutus.html/',views.about),
    path('contact.html/',views.contact),
    path('online.html/',views.online),
    path('paper.html/',views.paper),
    path('online.html/payment.html/',views.payment),
    path('service.html/',views.service),
    path('signup.html/',views.signup),
    path('signup.html/register/',views.register),
    path('sdp.html/',views.sdp),
    path('paper.html/payment2.html/',views.payment2),
    path('admin.html/',views.admin),
    path('progress.html/',views.progress),
    path('table/',views.table),
    path('branches.html/',views.branches),

]
