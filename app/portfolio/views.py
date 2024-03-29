from django.shortcuts import render
from django.http import HttpResponse

from .models import Menu
from .models import Person
from .models import Email
from .models import Website
from .models import Phone
from .models import Education
from .models import WorkExperience
from .models import Publication
from .models import Project
from .models import Skill
from .models import Picture
from .models import Portrait


def index(request):
    menu = Menu.objects.order_by('order')
    # person = Person.objects.order_by('last_name')
    person = Person.objects.filter(id=1)
    emails = Email.objects.filter(person_id=1).order_by('email')
    websites = Website.objects.filter(person_id=1).order_by('website')
    phones = Phone.objects.filter(person_id=1).order_by('phone')
    education = Education.objects.filter(person_id=1).order_by('-start_date')
    experience = WorkExperience.objects.filter(person_id=1).order_by('-start_date')
    publications = Publication.objects.filter(person_id=1).order_by('-release_date')
    projects = Project.objects.filter(person_id=1)
    skills = Skill.objects.filter(person_id=1)
    pictures = Picture.objects.filter(person_id=1)
    portrait = Portrait.objects.filter(person_id=1).first
    context = {
        'menu_list': menu,
        'person': person,
        'emails': emails,
        'websites': websites,
        'phones': phones,
        'education': education,
        'experience': experience,
        'publications': publications,
        'projects': projects,
        'skills': skills,
        'pictures': pictures,
        'portrait': portrait,
    }
    return render(request, 'portfolio/index.html', context)


def detail(request, menu_item):
    return HttpResponse("<h2>Content for menu item %s.</h2>" % menu_item)
