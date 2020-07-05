from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Event
from .forms import EventForm #EVENT
from .forms import PostForm
from .models import Comment #KOMMENTAR
from .forms import CommentForm #KOMMENTAR
from django.shortcuts import redirect
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active=True) #KOMMENTAR
    new_comment = None #KOMMENTAR
    if request.method == 'POST': #KOMMENTAR
        form = CommentForm(request.POST) #KOMMENTAR
        if form.is_valid(): #KOMMENTAR
            new_comment = form.save(commit=False) #KOMMENTAR
            new_comment.post = post #KOMMENTAR
            new_comment.save() #KOMMENTAR
    else: #KOMMENTAR
        form = CommentForm() #KOMMENTAR
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'new_comment': new_comment, 'form': form}) #KOMMENTAR


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)#request.FILES ist für Bilder notwendig
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form},)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post) #request.FILES ist für Bilder notwendig
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

######################
#      EVENT         #
######################

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'blog/event_detail.html', {'event': event})

def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.publish()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'blog/event_edit.html', {'form': form})

def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event) 
        if form.is_valid():
            event = form.save(commit=False)
            event.published_date2 = timezone.now()
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'blog/event_edit.html', {'form': form})

def events(request):
    events = Event.objects.filter(veranstaltungsdatum__gte=timezone.now()).order_by('veranstaltungsdatum')
    return render(request,'blog/events.html', {'events': events})

######################
#      ÜBER MICH     #
######################

def ubermich(request):
    return render(request, 'blog/ubermich.html')

#def urbangardening(request):
 #   return render(request, 'blog/urbangardening.html')

######################
#      START         #
######################

def startseite(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:3]
    events = Event.objects.filter(veranstaltungsdatum__gte=timezone.now()).order_by('veranstaltungsdatum')[0:3]
    return render(request, 'blog/startseite.html',  {'posts': posts}, {'events': events})
