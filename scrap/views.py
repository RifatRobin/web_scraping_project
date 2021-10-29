from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

#to use beautifulsoup4 for scraping we need to have these libraries in our code
import bs4
from bs4 import BeautifulSoup as bs
import urllib


# created view for the scraping process
def data_input(request):
    # the web address link will store in this variable
    web_address = request.POST.get('web_link', 'default')
    print(web_address)  # for checking purpose , will remove it later

    # the tag will store in this variable
    scrap_tag = request.POST.get('tag_code', 'default')
    print(scrap_tag)


    if request.method == 'POST':
        with urllib.request.urlopen(web_address) as response:
            html = response.read()
        text = str(html)
        soup = bs4.BeautifulSoup(text, 'html.parser')
        print(soup.find_all(scrap_tag))

    return render(request, "scrap/index.html")
