from django.shortcuts import render, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist

from .forms import URLForm
from .models import URL
from .common import generate_url_shortcut


def index(request):
    """
    Main page view.
    If received request was GET type, there is a form shown.
    If received request was POST type, there are two possibilities:
        - if form was filled out correctly, the result will be rendered
          as an output.
        - if form was invalid, there will be an error shown.
    :param request: received request.
    :return: rendered page, depending on taken action.
    """

    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            original_url = clean_data['url']
            url_hash = generate_url_shortcut(original_url)
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
    """
    View used for redirecting to the desired webpage. In case of incorrect
    shortcut (when it doesn't exist in the database), 404 code is returned.
    :param request: received request.
    :param short_url: shortcut passed by URL.
    :return: redirect to the original site or error response.
    """

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
