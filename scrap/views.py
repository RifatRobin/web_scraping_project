from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# to use beautifulsoup4 for scraping we need to have these libraries in our code
import bs4
from bs4 import BeautifulSoup as bs
import urllib


# created view for the scraping process of without tag attribute
def data_input(request):
    extracted_data = []
    if request.method == 'POST':
        # the web address link will store in this variable
        web_address = request.POST.get('web_link', 'default')

        # the tag will store in this variable
        scrap_tag = request.POST.get('tag_code', 'default')

        # code for the scraping process
        with urllib.request.urlopen(web_address) as response:
            html = response.read()
        scrapval = bs4.BeautifulSoup(html, 'html.parser')
        for data in scrapval.find_all(scrap_tag):
            desired_values = data.get_text()
            extracted_data.append(desired_values)
    return render(request, "scrap/index.html", {'extracted_data': extracted_data})


# created view for the scraping process for tag attribute
def with_attributes(request):
    extracted_data = []
    if request.method == 'POST':
        # the web address link will store in this variable
        web_address = request.POST.get('web_link', 'default')

        # the tag will store in this variable
        scrap_tag = request.POST.get('tag_code', 'default')
        tag_attribute = request.POST.get('attribute', 'default')

        # code for the scraping process
        with urllib.request.urlopen(web_address) as response:
            html = response.read()
        scrapval = bs4.BeautifulSoup(html, 'html.parser')

        for data in scrapval.find_all(scrap_tag):
            desired_values = data.get(tag_attribute)
            extracted_data.append(desired_values)

    return render(request, "scrap/index.html", {'extracted_data': extracted_data})
