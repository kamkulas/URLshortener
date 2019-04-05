"""
File storing forms classes.
"""

from django import forms


class URLForm(forms.Form):
    """
    Form used for taking user's inpu - URL that has to be shortened.
    """

    url = forms.URLField(widget=forms.URLInput(
        attrs={'placeholder': 'Paste your URL here', 'class': 'url-field'}))
