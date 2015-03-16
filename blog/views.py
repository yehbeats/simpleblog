from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.core.urlresolvers import reverse

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, id):
	post = Post.objects.get(pk=id)
	return render(request, 'blog/post_detail.html', {'post': post})


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


def post_edit(request, id):
	post = Post.objects.get(pk=id)

	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
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