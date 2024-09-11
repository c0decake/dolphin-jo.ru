from django import forms
from django.contrib.auth import get_user_model


class RegisterUser(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    password_2 = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    father_name = forms.CharField(max_length=100, required=False)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'password_2', 'last_name', 'first_name', 'father_name']

    def clean_password_2(self):
        c_data = self.cleaned_data
        if c_data['password_2'] != c_data['password']:
            raise forms.ValidationError('Пароли не совпадают!')
        else:
            return c_data['password_2']

    def clean_login(self):
        model = get_user_model()
        login = self.cleaned_data.get('login')
        if model.objects.filter(login=login):
            raise forms.ValidationError('Данный номер телефона уже занят')
        else:
            return login
