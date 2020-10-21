from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import hashlib

class Event(models.Model):
	name = models.CharField(max_length=20)
	place = models.CharField(max_length=32)
	date = models.DateField(default=timezone.now)
	logo = models.ImageField(upload_to="logo/")

	def save(self, *args, **kwargs):
		if not self.pk and Event.objects.exists():
			raise ValueError("Only One Event is permitted.")
		super().save(*args, **kwargs)

class TicketType(models.Model):
	name = models.CharField(max_length=20, unique=True)
	price = models.FloatField(null=False, blank=False)
	consommable = models.FloatField(default=0)

	def __str__(self):
		return self.name

class Ticket(models.Model):
	ticket_type = models.ForeignKey(TicketType, verbose_name='type', on_delete=models.CASCADE)
	consommable = models.FloatField(default=0)
	autres = models.TextField(blank=True, null=True)

	def save(self, *args, **kwargs):
		if not(self.pk): self.consommable = self.ticket_type.consommable
		super().save(*args, **kwargs)

	def __str__(self):
		return self.ticket_type.name

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to="profiles/")
	phone = models.CharField(max_length=16, unique=True, blank=False)
	date = models.DateField(default=timezone.now)
	ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
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

	class Meta:
		ordering = "-date", 

class Payment(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	somme = models.PositiveIntegerField(null=False, blank=False)
	date = models.DateTimeField(default=timezone.now)
	autres = models.TextField(blank=True, null=True)

	def save(self, *args, **kwargs):
		super(Payment, self).save(*args, **kwargs)
		ticket = self.profile.ticket
		ticket.consommable += self.somme
		ticket.save()

	def __str__(self):
		return f'{self.profile} : {self.somme}'

class Product(models.Model):
	name = models.CharField(max_length=20)
	price = models.PositiveIntegerField(null=False, blank=False)

	def __str__(self):
		return f'{self.name} : {self.price}'

class Consommation(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(null=False, blank=False)
	when = models.DateTimeField(default=timezone.now)

	def save(self, *args, **kwargs):
		ticket = self.profile.ticket
		ticket.consommable-=self.product.price*self.quantity
		if(ticket.consommable>0):
			ticket.save()
			super(Consommation, self).save(*args, **kwargs)

	def __str__(self):
		return f'{self.profile} : {self.product}'