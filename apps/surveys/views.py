from __future__ import unicode_literals
from django.shortcuts import render, redirect

def index(request):
    if 'attempt' in request.session:    
        request.session['attempt'] = request.session['attempt'] + 1
    else:
        request.session['attempt'] = 1
    return render(request, "surveys/index.html")

def process(request):
    context = {
        "attempt": request.session['attempt'],
        "name": request.POST['name'],
        "location": request.POST['location'],
        "language": request.POST['language'],
        "comment": request.POST['comment'],
    }
    return render(request, "surveys/result.html", context)


