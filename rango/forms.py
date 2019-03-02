from django import forms
from django.contrib.auth.models import User
from rango.models import Category, Page, UserProfile,PostAd,ContactProfile

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="please enter the category name")

    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # an inline class to provide additional information on the form
    class Meta:
        # provide an association between the modelform and a model
        model = Category
        fields = ("name",)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="please enter the title of the page")
    url = forms.URLField(max_length=128, help_text="please enter the url of the page")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ("category",)

    def clean(self):
        cleaned_data = self.cleaned_data

        url = cleaned_data.get('url')
        # If url is not empty and doesn't start with 'http://',
        # then prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
            return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


# ===================================
class PostForm(forms.ModelForm):

    class Meta:
        model = PostAd
        fields = ('title', 'image', 'description',"price")


class ContactProfileForm(forms.ModelForm):
    class Meta:
        model = ContactProfile
        fields = ('location', 'email', 'phone')