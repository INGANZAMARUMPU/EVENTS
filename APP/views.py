from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.contrib import messages

from .forms import *
from API.models import *

class Home(LoginRequiredMixin, View):
	template_name = "home.html"
	def get(self, request):
		clients = Profile.objects.all()
		form = ProfileForm()
		return render(request, self.template_name, locals())

	def post(self, request):
		form = ProfileForm(request.POST, request.POST, request.FILES)
		if form.is_valid():
			profile = form.save(commit=False)
			username = form.cleaned_data['phone']
			firstname = form.cleaned_data['firstname']
			lastname = form.cleaned_data['lastname']
			password = "no password"
			user = User.objects.create_user(username=username,password=password)
			user.first_name, user.last_name = firstname, lastname
			user.save()
			profile.user = user
			profile.save()
		clients = Profile.objects.all()
		return render(request, self.template_name, locals())

class EditProfile(LoginRequiredMixin, View):
	template_name = "home.html"
	def get(self, request, profile_id):
		clients = Profile.objects.all()
		profile = get_object_or_404(Profile, id=profile_id)
		form = ProfileForm(instance=profile)
		return render(request, self.template_name, locals())

	def post(self, request, profile_id):
		profile = get_object_or_404(Profile, id=profile_id)
		form = ProfileForm(request.POST, request.FILES, instance=profile)
		
		if form.is_valid():
			user = profile.user
			user.username = form.cleaned_data['phone']
			user.first_name = form.cleaned_data['firstname']
			user.last_name = form.cleaned_data['lastname']
			user.save()

			new_profile = form.save(commit=False)
			profile = new_profile;
			profile.user = user
			profile.save()
			return redirect("home")

		clients = Profile.objects.all()
		return render(request, self.template_name, locals())

class DeleteProfile(LoginRequiredMixin, View):
	template_name = "home.html"
	def get(self, request, profile_id):
		clients = Profile.objects.all()
		profile = get_object_or_404(Profile, id=profile_id)
		form = ProfileForm(instance=profile)
		delete = True
		return render(request, self.template_name, locals())

	def post(self, request, profile_id):
		profile = get_object_or_404(Profile, id=profile_id)
		form = ProfileForm(request.POST, request.FILES, instance=profile)
		
		if form.is_valid:
			user = profile.user
			user.delete()
			return redirect("home")

		clients = Profile.objects.all()
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