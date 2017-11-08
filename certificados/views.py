# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,HttpResponse
from .forms import UploadFileForm
from django.conf import settings
from gestiona_iesgn.views import test_login
from wsgiref.util import FileWrapper
from django.core.mail import EmailMessage
import os
import os.path
# Create your views here.

def add(request):
	test_login(request)
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES["csr"],request.session["username"])
			asunto="Petición de certificado de %s"%request.session["username"]
			cuerpo="El usuario %s ha subido un fichero csr:%s al programa gestiona, para gestionar la firma de su certificado."%(request.session["username"],request.FILES["csr"].name)
			email = EmailMessage(
 				   asunto,
				   cuerpo,
    				'informatica@gonzalonazareno.org',
				    ['informatica@gonzalonazareno.org'],
				    [],
				    reply_to=['informatica.gonzalonazareno.org'],
				    )
			email.send()
			return redirect(settings.SITE_URL+'/certificados')
	else:
		path= os.path.join(settings.BASE_DIR, 'cert/%s'%request.session["username"])
		if  os.path.isdir(path):
			files=os.listdir(path)
			paths=[]
			for file in files:
				paths.append(settings.SITE_URL+"/certificados/"+request.session["username"]+"/"+file)
			return render(request, 'files.html', {'files': files,'paths':paths})
		else:
			form = UploadFileForm()
			return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f,nombre):
	path= os.path.join(settings.BASE_DIR, 'cert/%s'%nombre)
	if not os.path.isdir(path):
		os.makedirs(path)
	path_file=path+"/"+f.name
	with open(path_file, 'w') as destination:
		destination.write(f.read())

def download(request,usuario,file):
	test_login(request)
	if usuario==request.session["username"]:
		filename = str(os.path.join(settings.BASE_DIR, 'cert/%s'%(request.session["username"]+"/"+file)))
		print "*"*20
		print filename
		f=open(filename,'r')
		wrapper = FileWrapper(f)
		response = HttpResponse(wrapper, content_type='text/plain')
		response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(filename)
		response['Content-Length'] = os.path.getsize(filename)
		return response
	else:
		return redirect(settings.SITE_URL)