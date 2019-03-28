
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from plenty_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plants/', views.PlantList.as_view()),
    path('plants/<int:id>', views.PlantView.as_view())
]
