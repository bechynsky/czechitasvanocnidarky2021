from django import forms

from vanocnidarky2021.app_vanocnidarky2021.models import Uzivatel, Instituce, Obdarovany

class RegistraceUzivatele(forms.ModelForm):
    class Meta:
        model = Uzivatel
        widgets = {
        'password': forms.PasswordInput(),
    }

class RegistraceInstituce(forms.ModelForm):
    class Meta:
        model = Instituce
        widgets = {
        'password': forms.PasswordInput(),
    }