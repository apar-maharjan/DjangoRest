from django.urls import path
from rest_framework.authtoken import views
from user_auth.api.v1.views.logout import user_logout

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('logout/', user_logout , name='logout'),

]