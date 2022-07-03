from django.shortcuts import render
import requests


# Create your views here.
def navbar(request):
    return render(request, "navbar.html")


def allnews(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=all"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records["alldata"] = inshorts_data
    return render(request, "all-news.html", records)


def business(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=business"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records["businessdata"] = inshorts_data
    return render(request, "business.html", records)


def sports(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=sports"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records["sportsdata"] = inshorts_data
    return render(request, "sports.html", records)


def entertainment(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=entertainment"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records["entertainmentdata"] = inshorts_data
    return render(request, "entertainment.html", records)