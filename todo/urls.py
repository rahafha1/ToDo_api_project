from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoViewSet, RegisterView

router = DefaultRouter()
router.register(r'todos', ToDoViewSet, basename='todo')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]
