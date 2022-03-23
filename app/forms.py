#este archivo se crea para crear formularios basados en tus models
from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm # para crear usuarios
from django.contrib.auth.models import User #para trabajar con el modelo predeterminado de usuario
from .validators import MaxSizeFileValidator #importo el validator q cree

class ContactoForm(forms.ModelForm): #crear clase para el formulario, siempre hereda de forms.Modelform

    class Meta: #clase para tomar el modelo con el q se va a relacionar
        model=Contacto
        #fields=['nombre','correo', 'tipo_consulta', 'mensaje', 'avisos']
        fields='__all__'

class AgregarProductoForm(forms.ModelForm):

    #agregando validaciones a algunos campos
    nombre = forms.CharField(min_length=3, max_length=50)
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])
    precio = forms.IntegerField(min_value=1, max_value=150000000)

    class Meta:
        model=Producto
        fields='__all__'

        widgets={
            "fecha_fab": forms.SelectDateWidget()
        }

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model=User
        fields=['username','first_name', 'last_name','email','password1', 'password2']



