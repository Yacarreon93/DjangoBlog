from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from .forms import PostForm

# Create your views here.


def post_create(request):
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Successfully created")
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request, "Not successfully created")
    # if request.method == "POST":
    #     print(request.POST.get("content"))
    #     title = request.POST.get("title")
    #     Post.objects.create(title=title)
    context = {
        "form": form
    }
    return render(request, "post_form.html", context)


def post_detail(request, id=None):
    # instance = Post.objects.get(id=6)
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": "Detail",
        "instance": instance
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    queryset = Post.objects.all()
    context = {
        "title": "List",
        "object_list": queryset
    }
    # if request.user.is_authenticated():
    #   context = {
    #       "title": "My user list"
    #   }
    # else:
    #   context = {
    #       "title": "List"
    #   }
    return render(request, "index.html", context)
    # return HttpResponse("<h1>List</h1>")


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Item saved", extra_tags='some-tag')
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request, "Item not saved")
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form
    }
    return render(request, "post_form.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Sucessfully deleted")
    return redirect("posts:list")
