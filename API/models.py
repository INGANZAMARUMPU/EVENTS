from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Ticket(models.Model):
	name = models.CharField(max_length=20)
	somme = models.PositiveIntegerField(null=False, blank=False)
	consommable = models.PositiveIntegerField(default=0)
	autres = models.TextField(blank=True, null=True)

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
	avatar = models.ImageField(upload_to="profiles/")
	phone = models.CharField(max_length=16, null=False, blank=False)
	mobile = models.CharField(max_length=16, blank=True, null=True)
	date = models.DateField(default=timezone.now)
	ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
	autres = models.TextField(blank=True, null=True)

class Payment(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	date = models.DateField(default=timezone.now)
	autres = models.TextField(blank=True, null=True)

	def recharge(self, montant:int):
		ticket = self.ticket
		ticket.consommable+=montant
		ticket.save()

class Product(models.Model):
	name = models.CharField(max_length=20)
	price = models.PositiveIntegerField(null=False, blank=False)

class Consommation(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	when = models.DateTimeField(default=timezone.now)