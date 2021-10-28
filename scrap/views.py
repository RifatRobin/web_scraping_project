from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def data_input(request):
    web_address = request.POST.get('web_link', 'default')
    print(web_address)

    scrap_tag = request.POST.get('tag_code', 'default')
    print(scrap_tag)

    return render(request,"scrap/index.html")