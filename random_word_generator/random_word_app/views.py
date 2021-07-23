from django.shortcuts import redirect, render, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    request.session['pageviews'] = 0
    return render(request, "home.html")

def random_word(request):
    context = {
        'word' : get_random_string(length=14, allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    }
    request.session['pageviews'] += 1
    return render(request, "random_word.html", context)

def reset(request):
    request.session['pageviews'] = 0
    return redirect('/random_word')
