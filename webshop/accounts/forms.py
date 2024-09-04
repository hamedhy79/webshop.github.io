from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import Customer


class UserRegisterForms(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'}))
    # password2 = forms.CharField(
    #     label='Password Again',
    #     widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your confirm Password'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username)
        if user:
            raise ValidationError(_("این نام کاربری از قبل وجود دارد"))
        return username


    # def clean(self):
    #     cd = super().clean()
    #     p1 = cd.get('password')
    #     p2 = cd.get('password2')
    #     if p1 and p2 and p2 != p1:
    #         raise ValidationError("رمز های عبور باید باهم برابر باشند")


class UserLoginForms(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'}))


# from django import forms
# from django.forms import ModelForm
# from .models import User
#
#
# class SignUp(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#     age = forms.IntegerField()
#
#     def __str__(self):
#         return f'{self.username}'
#
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#
#     def clean_password2(self):
#         password = self.cleaned_data.get("password")
#         password2 = self.cleaned_data.get("password2")
#         if password and password2 and password != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password'])
#         if commit:
#             user.save()
#         return user
