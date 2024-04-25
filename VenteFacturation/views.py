from django.shortcuts import render

def index(request, a, b):
    return render(request, "index.html", locals())