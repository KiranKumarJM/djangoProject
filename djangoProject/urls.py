from django.contrib import admin
from django.urls import include, path
from login import views

urlpatterns = [
    #path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('users/', views.userList.as_view()),
]