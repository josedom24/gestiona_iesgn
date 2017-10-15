from django.shortcuts import render
from gestiona_iesgn.views import test_profesor
import requests
import json
url_base="https://dit.gonzalonazareno.org/redmine/"

# Create your views here.


def inicio(request):
	test_profesor(request)
	r=requests.get(url_base+'projects.json',auth=(request.session["username"],request.session["password"]),verify=False)
	if r.status_code == 200:
		doc=r.json()
		info={"proyectos":doc["projects"]}
		return render("proyectos.html",info)