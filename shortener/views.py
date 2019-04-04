from hashlib import sha1
from base64 import urlsafe_b64encode

from django.shortcuts import render, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist

from .forms import URLForm
from .models import URL


def index(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            original_url = clean_data['url']
            hasher = sha1(original_url.encode())
            try:
                next_id = URL.objects.latest('id').id + 1
            except ObjectDoesNotExist:
                next_id = 1
            url_hash = urlsafe_b64encode(hasher.digest())[:10-len(str(next_id))].decode() + str(next_id)
            shortened_url, _ = URL.objects.get_or_create(original_path=original_url, defaults={'shortcut': url_hash})
            return render(request, 'result.html', {'absolute_path': request.build_absolute_uri(url_hash)})
        else:
            message = 'Form is not valid. Try again.'
            return render(request, 'error.html', {'error': message})
    else:
        print('--------->', reverse('main_page'))
        form = URLForm()
        return render(request, 'index.html', {'form': form})


def shortcut(request, short_url):
    try:
        original_url = URL.objects.get(shortcut=short_url).original_path
        return redirect(original_url)
    except ObjectDoesNotExist:
        return render(request, 'error.html', {'error': 'There is no such shortcut.'})
