from django.contrib.auth.models import User
from django.views.generic import FormView
from offline_messages.forms import OfflineGroupMessageForm
from offline_messages.utils import create_offline_message
from offline_messages.models import OfflineExpiration


class OfflineGroupMessageView(FormView):
    form_class = OfflineGroupMessageForm
    template_name = "send_group_message.html"

    def form_valid(self, form):
        message_kwargs = {'level' : form.cleaned_data['level']}
        if form.cleaned_data['expiration']:
            message_kwargs['content_object'] = OfflineExpiration.objects.create(datetime=form.cleaned_data['expiration'])
        if form.cleaned_data['groups']:
            users = User.objects.filter(groups__in=form.cleaned_data['groups']).distinct()
        else:
            users = User.objects.all()
        for user in users:
            create_offline_message(user, form.cleaned_data['message'], **message_kwargs)
        return super(OfflineGroupMessageView, self).form_valid(form)
