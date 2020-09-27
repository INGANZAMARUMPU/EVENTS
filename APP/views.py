import re
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib import messages
from os import popen

from .forms import *
from API.models import *

def getIps():
	ip_adresses = re.findall(r"\b(?:(?!255)[0-9]{1,3}\.){3}[0-9]{1,3}\b", popen("ipconfig").read())
	if not ip_adresses:
		ip_adresses = re.findall(r"\b(?:(?!255)[0-9]{1,3}\.){3}[0-9]{1,3}\b", popen("ifconfig").read())
	return ip_adresses;

class Home(LoginRequiredMixin, View):
	template_name = "home.html"
	def get(self, request):
		ip_adresses = getIps()
		clients = Profile.objects.all()[:10]
		form = ProfileForm()
		return render(request, self.template_name, locals())

	def post(self, request):
		form = ProfileForm(request.POST, request.POST, request.FILES)
		ip_adresses = getIps()
		if form.is_valid():
			profile = form.save(commit=False)
			username = form.cleaned_data['phone']
			firstname = form.cleaned_data['firstname']
			lastname = form.cleaned_data['lastname']
			ticket_type = form.cleaned_data['ticket_type']
			password = "no password"

			user = User.objects.create_user(username=username,password=password)
			user.first_name, user.last_name = firstname, lastname
			user.save()

			ticket_type = TicketType.objects.get(name=ticket_type)
			ticket = Ticket(ticket_type=ticket_type)
			ticket.save()

			profile.user = user
			profile.ticket = ticket
			profile.save()
			return redirect("/")
		clients = Profile.objects.all()[:10]
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
			ticket = profile.ticket
			ticket_type = form.cleaned_data['ticket_type']
			if ticket.consommable == ticket.ticket_type.consommable:
				if ticket.ticket_type != ticket_type:
					ticket.ticket_type = ticket_type
					ticket.consommable = ticket_type.consommable
					ticket.save()

				user = profile.user
				user.username = form.cleaned_data['phone']
				user.first_name = form.cleaned_data['firstname']
				user.last_name = form.cleaned_data['lastname']
				user.save()

				new_profile = form.save(commit=False)
				profile = new_profile;
				profile.user = user
				profile.save()
			else:
				print("ticket déjà utilisé. il ne peut plus être modifié!")
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