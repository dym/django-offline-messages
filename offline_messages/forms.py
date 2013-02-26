from django import forms
from django.contrib.auth.models import Group


class OfflineGroupMessageForm(forms.Form):
    groups = forms.ModelMultipleChoiceField(Group.objects, required=False)
    message = forms.CharField(widget=forms.Textarea())
    expiration = forms.DateTimeField(required=False)
