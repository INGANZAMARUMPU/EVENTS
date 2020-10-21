from admin_totals.admin import ModelAdminTotals
from django.contrib import admin
from django.db.models import Sum
from django.db.models.functions import Coalesce
from .models import *

class ProfileAdmin(ModelAdminTotals):
	list_display = "user", "avatar", "phone", "ticket", "date", "autres"
	list_filter =  "user", "avatar", "phone", "ticket__ticket_type", "date"
	ordering =  "user", "avatar", "phone", "ticket", "date"
	readonly_fields = ['ticket']
	list_totals = [
		('ticket', lambda field: Coalesce(Sum(f"{field}__ticket_type__price"), 0)),
		# ('col_c', Avg)
	]

class TicketTypeAdmin(admin.ModelAdmin):
	list_display = "name", "price", "consommable"
	list_filter = "name", "price", "consommable"
	ordering = "name", "price", "consommable"

class PaymentAdmin(ModelAdminTotals):
	fields = "profile", "somme",
	list_display = "profile", "phone","somme", "date", "autres"
	list_filter = "profile", "somme", "date", "autres"
	search_fields = "profile__phone", "profile__user__first_name", "profile__user__last_name"
	list_totals = [
		('somme', lambda field: Coalesce(Sum(field), 0)),
		# ('col_c', Avg)
	]
	ordering = "profile", "somme", "date", "autres"

	def phone(self, obj):
		return f"{obj.profile.phone}"

class EventAdmin(admin.ModelAdmin):
	list_display = "name", "place", "date", "logo"
	list_filter ="name", "place", "date", "logo"
	ordering ="name", "place", "date", "logo"

class ProductAdmin(admin.ModelAdmin):
	list_display = "name", "price"
	list_filter ="name", "price"
	ordering ="name", "price"

class ConsommationAdmin(admin.ModelAdmin):
	list_display = "product", "quantity","profile" ,"when" 
	list_filter = "product", "quantity","profile" ,"when" 
	ordering = "product", "quantity","profile" ,"when" 

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(TicketType, TicketTypeAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Consommation, ConsommationAdmin)