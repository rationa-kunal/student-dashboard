from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Subject, LinkWrapper, Link, Like, Dislike


def list_subject(request):
    subjects = Subject.objects.all()
    html = ""
    for subject in subjects:
        wrappers = subject.linkwrapper_set.all()
        html+=subject.title
        for wrapper in wrappers:
            html+= "<br><br>"
            html+=wrapper.title
            html+= "<br>"
            html+=str(wrapper.id) +"  "+ "<a href="+ str(wrapper.id) +">link</a>"

    context = {
        'subjects' : Subject.objects.all(),
    }
    return render(request, 'subject/subject_list.html', context)




def list_links(request, wrapper_id):
    wrapper = LinkWrapper.objects.get(id=wrapper_id)
    links = wrapper.link_set.all()
    # likes = request.user.like_set.all()
    context = {
        'wrapper_id' : wrapper_id,
        'links' : links,
        'wrapper' : wrapper,
    }
    return render(request, 'subject/link_list.html', context)



@login_required()
def like(request, wrapper_id, link_id):
    new_like, created = Like.objects.get_or_create(user=request.user, link=get_object_or_404(Link, pk=link_id))
    return redirect('list_of_links', wrapper_id=wrapper_id)


@login_required()
def dislike(request, wrapper_id, link_id):
    new_like, created = Dislike.objects.get_or_create(user=request.user, link=get_object_or_404(Link, pk=link_id))
    return redirect('list_of_links', wrapper_id=wrapper_id)
