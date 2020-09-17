from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import hashlib

class Ticket(models.Model):
	name = models.CharField(max_length=20)
	somme = models.PositiveIntegerField(null=False, blank=False)
	consommable = models.PositiveIntegerField(default=0)
	autres = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to="profiles/")
	phone = models.CharField(max_length=16, unique=True, blank=False)
	mobile = models.CharField(max_length=16, blank=True, null=True)
	date = models.DateField(default=timezone.now)
	ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
	autres = models.TextField(blank=True, null=True)
	qr = models.CharField(max_length=64, null=False, editable=False)

	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name}"

	def first_name(self):
		return f"{self.user.first_name}"

	def last_name(self):
		return f"{self.user.last_name}"

	def save(self, *args, **kwargs):
		infos = f"{self.phone}{self.date}"
		self.qr = hashlib.sha224(infos.encode()).hexdigest()
		super(Profile, self).save(*args, **kwargs)

class Payment(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	somme = models.PositiveIntegerField(null=False, blank=False)
	date = models.DateField(default=timezone.now)
	autres = models.TextField(blank=True, null=True)

	def recharge(self, montant:int):
		ticket = self.ticket
		ticket.consommable+=montant
		ticket.save()

	def __str__(self):
		return f'{self.profile} : {self.somme}'

class Product(models.Model):
	name = models.CharField(max_length=20)
	price = models.PositiveIntegerField(null=False, blank=False)

	def __str__(self):
		return f'{self.profile} : {self.name}'

class Consommation(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	when = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.profile} : {self.product}'