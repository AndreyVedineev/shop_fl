from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "title": "Главная",
        "content": "Магазин цветов BOUQUET №1",
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "О нас",
        "content": "О нас",
        "text_on_page": 'The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.',
    }
    return render(request, "main/about.html", context)
