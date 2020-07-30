from django.contrib import admin
from django.urls import path, path
from contactapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/get/', views.contact_list, name="contact-list"),
    path('api/get/<str:id>', views.contact_detail, name="contact-detail"),

    path('api/post', views.contactCreate, name="contactCreate"),

]
