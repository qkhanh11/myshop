from django import forms
from django.contrib.auth.models import User
import re


class RegisterForm(forms.Form):
    username = forms.CharField(label="Tài khoản", max_length=50, required=True)
    password1 = forms.CharField(label="Mật khẩu", required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Xác nhận mật khẩu", widget=forms.PasswordInput, required=False)
    email = forms.EmailField(label="Email")
    last_name = forms.CharField(label="Họ")
    first_name = forms.CharField(label="Tên")

    def clean_password2(self):
        if "password1" in self.cleaned_data:
            password1 = self.cleaned_data["password1"]
            password2 = self.cleaned_data["password2"]
            if password1 and password1 == password2:
                return password2
            raise forms.ValidationError("Mật khẩu không hợp lệ")
        
    def clean_username(self):
        username = self.cleaned_data["username"]
        # if re.search(r'^[A-Za-z0-9]+(?:[_-][A-Za-Z0-9]+)*$', username):
        #     raise forms.ValidationError("Username không hợp lệ")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("username đã tồn tại trong hệ thống")
    
    def save(self):
        User.objects.create_user(
            username = self.cleaned_data['username'],
            password = self.cleaned_data['password1'],
            email=self.cleaned_data['email'],
            last_name = self.cleaned_data['last_name'],
            first_name = self.cleaned_data['first_name'],
            # is_staff = True

        )