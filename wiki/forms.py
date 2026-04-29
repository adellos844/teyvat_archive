from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil
from .utils import obtener_datos_enka

class RegistroForm(UserCreationForm):
    uid = forms.CharField(max_length=9, min_length=9, label="Tu UID de Genshin")
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'uid')

    def clean_uid(self):
        uid = self.cleaned_data['uid']
        
        if Perfil.objects.filter(uid_genshin=uid).exists():
            raise forms.ValidationError("Ya existe un perfil con este UID.")
        
        datos = obtener_datos_enka(uid)
        if 'error' in datos:
            raise forms.ValidationError("El UID no es válido o el perfil es privado. Asegúrate de tener el perfil visible en Genshin Impact.")
        
        return uid

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Perfil.objects.create(usuario=user, uid_genshin=self.cleaned_data['uid'])
        return user