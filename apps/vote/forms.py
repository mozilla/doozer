from django import forms

from vote.models import Vote


class VoteForm(forms.ModelForm):
    class Meta(object):
        model = Vote
        exclude = ('creator')
