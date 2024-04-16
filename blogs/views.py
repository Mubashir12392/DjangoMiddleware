from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Post

# Create your views here.

class Homepage(View):
    def get(self, request):
        return HttpResponse('Hello from me')
    
class Post_detail(View):
    def get(self, request):
        objs = Post.objects.get(id=1)
        return HttpResponse(objs)