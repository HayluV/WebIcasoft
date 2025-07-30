from appIcasoftWeb.models import User
from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['dni','username', 'first_name','last_name', 'email', 'telefono', 'password']
        widgets = {
            'dni': forms.TextInput(attrs={
                'id': 'documento',
                'class': 'form-input',
                'placeholder': 'Ingrese su número de identidad',
                'maxlength': '8'
            }),
            'username': forms.TextInput(attrs={
                'id': 'username',
                'class': 'form-input',
                'placeholder': 'Ingrese su nombre de usuario',
            }),
            'first_name': forms.TextInput(attrs={
                'id': 'nombre',
                'class': 'nombreDNI form-input',
                'placeholder': 'Ingrese su nombre',
                'required': True,
            }),
            'last_name': forms.TextInput(attrs={
                'id': 'apellidos',
                'class': 'apellidoDNI form-input',
                'placeholder': 'Ingrese sus apellidos',
            }),
            'email': forms.EmailInput(attrs={
                'id': 'correo',
                'class': 'form-input',
                'placeholder': 'Ingrese su correo electrónico',
                'required': True,
                'autocomplete': 'off'
            }),
            'telefono': forms.TextInput(attrs={
                'id': 'celular',
                'class': 'form-input',
                'placeholder': 'Ingrese su número de celular',
                'autocomplete': 'off'
            }),
            'password': forms.PasswordInput(attrs={
                'id': 'contrasena',
                'class': 'form-input',
                'placeholder': 'Cree una contraseña',
                'required': True,
                'minlength': '8',
                'maxlength': '20',
                'autocomplete': 'new-password'
            }),
        }