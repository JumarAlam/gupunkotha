from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import generic

from messaging.forms import MessageCreateForm
from messaging.models import Message


class MessageListView(LoginRequiredMixin, generic.ListView):
    model = Message
    template_name = 'message-list.html'

    def get_queryset(self):
        return super().get_queryset().filter(to=self.request.user).order_by('-on')


class MessageCreateView(generic.CreateView):
    model = Message
    form_class = MessageCreateForm
    template_name = 'message-form.html'

    def get_success_url(self):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "Message successfully sent.",
            extra_tags="alert alert-success"
        )
        return self.request.path

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['to'] = get_object_or_404(get_user_model(), username=self.kwargs.get('username'))

        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['to'] = get_object_or_404(get_user_model(), username=self.kwargs.get('username'))
        return context
