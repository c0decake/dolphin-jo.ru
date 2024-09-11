from django import forms
from django.apps import apps
from django.contrib.auth import get_user_model

from .models import Orders, Shop


class NewOrderForm(forms.ModelForm):
    work_date = forms.DateField()
    time_in = forms.TimeField()
    time_out = forms.TimeField()
    rating = forms.IntegerField()
    shop = forms.IntegerField()
    price = forms.IntegerField()
    post = forms.IntegerField()
    taxi_to = forms.BooleanField(required=False)
    taxi_from = forms.BooleanField(required=False)
    food = forms.BooleanField(required=False)
    drinks = forms.BooleanField(required=False)
    toilet = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        self.user_id = kwargs.pop('user_id', None)

        super(NewOrderForm, self).__init__(*args, **kwargs)

        self.fields['author'] = forms.IntegerField(initial=self.user_id, required=False)

    def clean(self):
        cleaned_data = super().clean()
        if self.user_id:
            model = get_user_model()
            cleaned_data['author'] = model.objects.get(pk=self.user_id)
        return cleaned_data

    class Meta:
        model = Orders
        fields = ['rating', 'shop', 'price', 'author', 'post', 'taxi_to', 'taxi_from', 'food', 'drinks', 'toilet',
                  'time_in', 'time_out', 'work_date']

    def clean_shop(self):
        shop_id = self.cleaned_data.get('shop')
        return Shop.objects.get(pk=shop_id)

    def clean_post(self):
        post_model = apps.get_model('accounts', 'Post')
        post_id = self.cleaned_data.get('post')
        return post_model.objects.get(pk=post_id)

    def clean_taxi_to(self):
        if self.cleaned_data.get('taxi_to'):
            return True
        else:
            return False

    def clean_taxi_from(self):
        if self.cleaned_data.get('taxi_from'):
            return True
        else:
            return False

    def clean_food(self):
        if self.cleaned_data.get('food'):
            return True
        else:
            return False

    def clean_drinks(self):
        if self.cleaned_data.get('drinks'):
            return True
        else:
            return False

    def clean_toilet(self):
        if self.cleaned_data.get('toilet'):
            return True
        else:
            return False

    def clean_time_in(self):
        time_in = self.cleaned_data.get('time_in')
        return time_in

    def save(self, commit=True):
        instance = super(NewOrderForm, self).save(commit=False)
        instance.author = self.cleaned_data['author']
        if commit:
            instance.save()
        return instance
