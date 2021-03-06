from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.widgets import HiddenInput,Textarea,TextInput
from usuarios.libldap import LibLDAP

def getSelect():
	ldap=LibLDAP()
	
	lista=ldap.buscar("(uid=*)",["uid","givenname","sn"])
	lista2=[]
	for usuario in lista:
		lista2.append((usuario["uid"][0],usuario["givenName"][0]+" "+usuario["sn"][0]))
		ldap.logout()
	return lista2

class CorreoForm(forms.Form):
	replyto=forms.CharField(required=False,max_length=100,widget=forms.TextInput(attrs={'class': "form-control"}))
	asunto=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': "form-control"}))
	contenido=forms.CharField(widget=forms.Textarea(attrs={'class': "form-control",'cols': 100, 'rows': 15}))
	def clean(self):
		super(CorreoForm, self).clean()
		asunto = self.cleaned_data.get("asunto")
		if not asunto:
			del self._errors['asunto']
		contenido = self.cleaned_data.get("contenido")
		if not contenido:
			del self._errors['contenido']

		return self.cleaned_data

class BuscarDestinatariosForm(forms.Form):
	
	def __init__(self, *args, **kwargs):
			dest = kwargs.pop('dest')
			alum = kwargs.pop('alum')
			
			super(BuscarDestinatariosForm, self).__init__(*args, **kwargs)
			lista=[("0","Ninguno"),
				('all','Todos'),
				("soloalumnos","Alumnos"),
				("asir1","1º ASIR"),
				("asir2","2º ASIR"),
				("smr1","1º SMR"),
				("smr2","2º SMR"),
				('tituladosasir', 'Titulados ASIR'),
    			('tituladossmr', 'Titulados SMR'),
    			('alltitulados', 'Todos los titulados'),
				("profesores","Profesores"),
				("antiguosprofesores","Antiguos Profesores"),
				('allprofesores','Todos los profesores'),
				('openstackusers','Usuarios OpenStack'),
				("antiguosalumnos","Otros Alumnos"),
				]
			
			self.fields["usuarios"] = forms.ChoiceField(initial=alum,choices=lista,required=False,widget=forms.Select(attrs={'class': "form-control",'onchange': 'this.form.submit();'}))
			self.fields["destinatarios"]=forms.MultipleChoiceField(initial=dest,choices=getSelect(),required=True,widget=forms.SelectMultiple(attrs={'class': "form-control js-example-basic-multiple"}))

			
