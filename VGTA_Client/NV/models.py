from django.db import models

# Create your models here.

from django import forms


class GetIpAddressForm(forms.Form):
    ip_address_field = forms.Field()
