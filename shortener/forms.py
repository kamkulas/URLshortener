from django import forms


class URLForm(forms.Form):
    url = forms.URLField(widget=forms.URLInput(
        attrs={'placeholder': 'Paste your URL here', 'class': 'url-field'}))
