from datetime import date
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render ,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Post
from .forms import commentForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

class StartingPageView(ListView):
    template_name="blog/index.html"
    model= Post
    ordering= ["-date"]
    context_object_name="posts"
    
    def get_queryset(self) :
        queryset=super().get_queryset()
        data=queryset[:3]
        return data



def get_date(post):
    return post['date']

# Create your views here.
class AllPostView(ListView):
    template_name="blog/all-posts.html"
    model=Post
    ordering=["-date"]
    context_object_name="all_posts"

class SinglePostView(View):
    
    
    def get(self,request,slug):
        post=Post.objects.get(slug=slug)
        context = { 
            "post": post,
            "post_tags":post.tags.all(),
            "comment_form": commentForm()
            } 
                  
        
    
        return render(request,"blog/post-detail.html",context)
    
    def post(self,request,slug):
        comment_form=commentForm(request.POST)
        if comment_form.is_valid():
            post=Post.objects.get(slug=slug)
            comment=comment_form.save(commit=False)
            comment.post=post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))
        
        
        post=Post.objects.get(slug=slug)
        context = { 
            "post": post,
            "post_tags":post.tags.all(),
            "comment_form": comment_form
            } 
        return render(request,"blog/post-detail.html",context)
    

        
        
    
    