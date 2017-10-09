# -*- coding: utf-8 -*-
from django import forms
clasesAlumnos = (
    ('0','Todos'),
    ('1', '1º ASIR'),
    ('2', '2º ASIR'),
    ('3', '1º SMR'),
    ('4', '2º SMR'),
    ('6', 'Antiguo Alumno'),
)

clasesProfesores = (
    ('0','Todos'),
    ('5', 'Profesor'),
    ('7', 'Antiguo Profesor'),
)


class BuscarUsuario(forms.Form):
    nombre=forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    apellidos=forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    #clase=forms.ChoiceField(choices=(),required=False,widget=forms.Select(attrs={'class': "form-control",'onchange': 'this.form.submit();'}))
    AP=forms.CharField(widget=forms.HiddenInput())
    def __init__(self, *args, **kwargs):
        super(BuscarUsuario, self).__init__(*args, **kwargs)
        if args[0].has_key("AP") and args[0]["AP"]=="profesores":
            self.fields['clase']=forms.ChoiceField(choices=clasesProfesores,required=False,widget=forms.Select(attrs={'class': "form-control",'onchange': 'this.form.submit();'}))

        else:
            self.fields['clase']=forms.ChoiceField(choices=clasesAlumnos,required=False,widget=forms.Select(attrs={'class': "form-control",'onchange': 'this.form.submit();'}))

class newUserForm(forms.Form):
    uid=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': "form-control"}))
    userpassword=forms.CharField(max_length=100,required=True,widget=forms.PasswordInput(attrs={'class': "form-control"}))
    givenname=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': "form-control"}))
    sn=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': "form-control"}))
    mail=forms.CharField(max_length=100,required=True,widget=forms.EmailInput(attrs={'class': "form-control"}))
    l=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': "form-control"}))
    AP=forms.CharField(widget=forms.HiddenInput())
    #description=forms.ChoiceField(choices=clasesAlumnos[1:],required=False,widget=forms.Select(attrs={'class': "form-control"}))
    def __init__(self, *args, **kwargs):
        super(newUserForm, self).__init__(*args, **kwargs)
        if args[0].has_key("AP") and args[0]["AP"]=="profesores":
            self.fields['description']=forms.ChoiceField(choices=clasesProfesores[1:],required=False,widget=forms.Select(attrs={'class': "form-control"}))

        else:
            self.fields['description']=forms.ChoiceField(choices=clasesAlumnos[1:],required=False,widget=forms.Select(attrs={'class': "form-control"}))


class updateUserForm(forms.Form):
    uid=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': "form-control",'readonly':'readonly'}))
    userpassword=forms.CharField(max_length=100,required=False,widget=forms.PasswordInput(attrs={'class': "form-control"}))
    givenname=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': "form-control"}))
    sn=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': "form-control"}))
    mail=forms.CharField(max_length=100,required=True,widget=forms.EmailInput(attrs={'class': "form-control"}))
    l=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': "form-control"}))
    homedirectory=forms.CharField(widget=forms.HiddenInput())
    #description=forms.ChoiceField(choices=clasesAlumnos[1:],required=False,widget=forms.Select(attrs={'class': "form-control"}))
    def __init__(self, *args, **kwargs):
        super(updateUserForm, self).__init__(*args, **kwargs)
        if args[0].has_key("AP") and args[0]["AP"]=="profesores":
            self.fields['description']=forms.ChoiceField(choices=clasesProfesores[1:],required=False,widget=forms.Select(attrs={'class': "form-control"}))

        else:
            self.fields['description']=forms.ChoiceField(choices=clasesAlumnos[1:],required=False,widget=forms.Select(attrs={'class': "form-control"}))
