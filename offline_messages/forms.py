from django import forms
from django.contrib.auth.models import Group
from django.contrib.messages import constants


class OfflineGroupMessageForm(forms.Form):
    MESSAGE_LEVELS = (
            (constants.INFO, "INFO"),
            (constants.DEBUG, "DEBUG"),
            (constants.SUCCESS, "SUCCESS"),
            (constants.WARNING, "WARNING"),
            (constants.ERROR, "ERROR"),
    )
    groups = forms.ModelMultipleChoiceField(Group.objects, required=False)
    message = forms.CharField(widget=forms.Textarea())
    expiration = forms.DateTimeField(required=False)
    level = forms.ChoiceField(MESSAGE_LEVELS)
