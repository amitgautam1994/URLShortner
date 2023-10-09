from django.shortcuts import render
from .models import ShortURL
from .forms import CreateNewShortURL
import random
import string


def home(request):
    return render(request, 'home.html')


def createShortURL(request):
    if request.method == "POST":
        form = CreateNewShortURL(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            random_char_list = list(string.ascii_letters)
            random_chars = ''
            for idx in range(6):
                random_chars += random.choice(random_char_list)

            while len(ShortURL.objects.filter(short_url=random_chars)) != 0:
                for idx in range(6):
                    random_chars += random.choice(random_char_list)

            url_obj = ShortURL(original_url=original_url,
                               short_url=random_chars)
            url_obj.save()
            return render(request, 'urlcreated.html', {"chars": random_chars})
    else:
        form = CreateNewShortURL()
        context = {'form': form}
        return render(request, 'create.html', context)


def redirectPage(request, url):
    current_obj = ShortURL.objects.filter(short_url=url).get()
    # print(current_obj.query)
    print(current_obj)
    if current_obj is None:
        return render(request, "pagenotfound.html")

    context = {
        'obj': current_obj
    }
    print(context)
    return render(request, "redirect.html", context)
