from django.shortcuts import render, render_to_response, get_object_or_404


def home(request):
    context = dict()
    return render_to_response('home.html', context)

