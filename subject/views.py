from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject, LinkWrapper, Link


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
    context = {
        'links' : links,
    }
    return render(request, 'subject/link_list.html', context)