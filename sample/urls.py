from django.urls import path
from sample.views import HelloWorld

urlpatterns = [
    path('hello_world', HelloWorld.as_view()),
]