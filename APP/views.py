from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.contrib import messages

from .forms import *

class Home(LoginRequiredMixin, View):
	template_name = "home.html"
	def get(self, request):
		form = ProfileForm(request.FILES)
		return render(request, self.template_name, locals())

	def post(self, request):
		form = ProfileForm(request.POST, request.FILES)
		return render(request, self.template_name, locals())

def deconnexion(request):
	logout(request)
	return redirect("login")

class Connexion(View):
	template_name = 'login.html'
	next_p = "home"

	def get(self, request, *args, **kwargs):
		form = ConnexionForm()
		try:
			self.next_p = request.GET["next"]
		except:
			print
		return render(request, self.template_name, locals())

	def post(self, request, *args, **kwargs):
		form = ConnexionForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user:  # Si l'objet renvoyé n'est pas None
				login(request, user)
				messages.success(request, "You're now connected!")
				return redirect(self.next_p)
			else:
				messages.error(request, "logins incorrect!")
		return render(request, self.template_name, locals())