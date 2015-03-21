from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, id):
	post = Post.objects.get(pk=id)
	return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('blog.views.post_detail', id=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, id):
	post = get_object_or_404(Post, pk=id)
	
	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			# post.delete()
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('blog.views.post_detail', id=post.pk) 
	else: 
		form = PostForm(instance=post)
	return render(request,'blog/post_edit.html', {'form': form})


def post_draft(request):
	posts=Post.objects.filter(published_date__isnull=True).order_by('-create_date')
	return render(request, 'blog/post_draft.html', {'posts': posts})

@login_required
def post_publish(request, id):
	post = Post.objects.get(pk=id)
	post.publish()
	return redirect('blog.views.post_detail', id=id)

@login_required
def post_remove(request, id):
	post = Post.objects.get(pk=id)
	post.delete()
	return redirect('blog.views.post_list')