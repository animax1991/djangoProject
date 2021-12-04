from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello</h1>")
    my_context = {
        "my_text":123,
        "my_list":[12,23,52]
    }
    return render(request, "home.html", my_context)