from django.shortcuts import render,get_object_or_404
from.forms import CommentForm
from django.http import HttpResponseRedirect
from.models import Post,Category
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

def blog_list (request):
    categories = Category.objects.all()
    posts=Post.objects.all()

    paginator=Paginator(posts,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context ={
        'posts':posts,
        'page_obj':page_obj,
        'categories':categories,
    }
    return render (request,'index.html',context)


def blog_details (request,slug):
    post=Post.objects.get (slug=slug)
    comments = post.comments.all()
    categories = Category.objects.all()
    similar_post = post.tages.similar_objects()[:4]

     
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            # redirect to a new URL:
            messages.success(request, 'Your comment submitted.')
            return HttpResponseRedirect(request.path_info)
    # if a GET (or any other method) we'll create a blank form
    else:
        comment_form = CommentForm()

    context ={
        'post':post,
        'comments':comments,
        'categories':categories,
        'similar_post':similar_post,
    }
    return render (request,'details.html',context)



def category (request, category_slug=None):
    category = None
    categories = Category.objects.all()
    posts = Post.objects.all()
    latest_post= Post.objects.all()[:3]

    paginator=Paginator(posts,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)

        paginator=Paginator(posts,3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    context={
        'posts':posts,
        'category': category,
        'categories': categories,
        'latest_post':latest_post,
        'page_obj':page_obj,


    }

    return render (request,'category.html',context)
   