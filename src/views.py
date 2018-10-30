from django.shortcuts import render
from django.contrib.auth import authenticate, login


def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            pass
    context = dict()
    return render(request, 'index/index.html', context)
