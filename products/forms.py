from django import forms


class GetFeedback(forms.Form):
    user_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
