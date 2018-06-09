from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def loginView(request):
    return render(request, "login.html")


def takeinput(request):
    mno = request.post["mobilenum"]
    print(mno)
    return HttpResponse("hello")