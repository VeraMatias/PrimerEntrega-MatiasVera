from django import forms

class Form_producto(forms.Form):
    txt_titulo = forms.CharField(label='Titulo', max_length=50)
    txt_descripcion = forms.CharField(label='Descripcion',max_length=200)
    int_precio = forms.IntegerField(label='Precio')


class Form_comprador(forms.Form):
    txt_nombre = forms.CharField(label='Nombre',max_length=50)
    int_DNI = forms.IntegerField(label='DNI',)
    txt_email = forms.EmailField(label='Email',)
    txt_contrasenia = forms.CharField(label='Contraseña',max_length=8)
    txt_direccion_de_envio = forms.CharField(label='Direccion de Envio',max_length=50)

class Form_vendedor(forms.Form):
    txt_nombre = forms.CharField(label='Nombre',max_length=50)
    int_DNI = forms.IntegerField(label='DNI',)
    txt_email = forms.EmailField(label='Email',)
    txt_contrasenia = forms.CharField(label='Contraseña',max_length=8)
