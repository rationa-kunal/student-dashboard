from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Subject, LinkWrapper, Link, Like, Dislike, Tag
from .forms import addLinkForm, addTagForm




def greeting(request):
    return render(request, 'subject/greeting.html', {})




def list_subject(request):
    subjects = Subject.objects.all()

    context = {
        'subjects' : Subject.objects.all(),
    }
    return render(request, 'subject/subject_list.html', context)





def list_links(request, wrapper_id):
    wrapper = get_object_or_404(LinkWrapper, pk=wrapper_id)
    subject = wrapper.subject
    links = wrapper.link_set.all()
    context = {
        'wrapper_id': wrapper_id,
        'links': links,
        'wrapper': wrapper,
        'subject': subject,
        'form': False,
    }

    if not request.user.has_perm('subject.add_link'):
        return render(request, 'subject/link_list.html', context)

    if request.method == "POST":
        form = addLinkForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            contributor = form.cleaned_data['contributor']
            link = form.cleaned_data['link']
            new_link = Link(title=title, description=description, link=link, linkwrapper=wrapper,
                            contributor=contributor)
            new_link.save()
            return redirect('list_of_links', wrapper_id=wrapper_id)

    else:
        form = addLinkForm()

    context['form'] = form

    return render(request, 'subject/link_list.html', context)





@login_required()
def like(request, wrapper_id, link_id):
    new_like, created = Like.objects.get_or_create(user=request.user, link=get_object_or_404(Link, pk=link_id))
    return redirect('list_of_links', wrapper_id=wrapper_id)


@login_required()
def dislike(request, wrapper_id, link_id):
    new_like, created = Dislike.objects.get_or_create(user=request.user, link=get_object_or_404(Link, pk=link_id))
    return redirect('list_of_links', wrapper_id=wrapper_id)




def link_detail(request, link_id):
    link = get_object_or_404(Link, pk=link_id)
    wrapper = link.linkwrapper
    subject = wrapper.subject
    wrapper_id = wrapper.pk
    form = False
    context = {
        'link' : link,
        'form' : False,
        'tags' : link.tag.all(),
        'subject' : subject,
        'wrapper' : wrapper,
    }

    if not request.user.has_perm('subject.add_link'):
        return render(request, 'subject/link_detail.html', context)

    if request.method == "POST":
        form = addTagForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            choices = {'IP': 'imp',
                       'PP': 'practical program',
                       'PT': 'practical theory',
                       'BF': 'by faculty',
                       'VV': 'verified',
                       'CL': 'cool',
                       'GH': 'good handwriting'}
            tag = get_object_or_404(Tag, title=choices[title])

            if tag in link.tag.all():
                return redirect('list_of_links', wrapper_id=wrapper_id)

            link.tag.add(tag)

            return redirect('list_of_links', wrapper_id=wrapper_id)

    else:
        form = addTagForm()

    context['form'] = form

    return render(request, 'subject/link_detail.html', context)




def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    tags = Tag.objects.all()
    links = tag.link_set.all()

    context = {
        'tag' : tag,
        'tags' : tags,
        'links' : links,
    }

    return render(request, 'subject/tag_detail.html', context)