from django.shortcuts import render
from django.views import View

# Create your views here.
class HelloWorld(View):
    def get(self, request):
        return render(request, 'hello_world.html')