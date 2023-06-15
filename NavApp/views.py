from django.shortcuts import render, redirect

from .models import Site


def first_page(request):
    return redirect('page/1')


def page(request, pk):
    nav_objects = Site.objects.values('id', 'site_nav', 'site_nav_position').filter(site_nav_position__gt=0).order_by(
        'site_nav_position')
    content_object = Site.objects.values().get(id=pk)
    context = {'pk': pk, 'nav_objects': nav_objects, 'content_object': content_object}
    return render(request, 'NavApp/page.html', context)


