from django import forms

from messaging.models import Message


class MessageCreateForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('message',)

    def save(self, commit=True):
        self.instance.to = self.to
        return super().save(commit)

    def __init__(self, *args, **kwargs):
        self.to = kwargs.pop('to')
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'class': 'form-control'})
