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
            next_id = len(URL.objects.all()) + 1
            url_hash = str(next_id) + '_' + urlsafe_b64encode(
                hasher.digest())[:10-len(str(next_id))].decode()
            shortened_url, created = URL.objects.get_or_create(
                original_path=original_url,
                defaults={'shortcut': url_hash}
            )
            if not created:
                url_hash = shortened_url.shortcut
            return render(
                request,
                'result.html',
                {'absolute_path': request.build_absolute_uri(url_hash)}
            )
        else:
            message = 'Form is not valid. Try again.'
            return render(request, 'error.html', {'error': message})
    else:
        form = URLForm()
        return render(request, 'index.html', {'form': form})


def shortcut(request, short_url):
    try:
        original_url = URL.objects.get(shortcut=short_url).original_path
        return redirect(original_url)
    except ObjectDoesNotExist:
        response = render(
            request,
            'error.html',
            {'error': 'Shortcut not found.'}
        )
        response.status_code = 404
        return response
