# blog/forms.py

from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class":"form-control", "placeholder":"Your Email"}
        )
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )
