from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
	list_display = "user", "avatar", "phone", "ticket", "date", "autres"
	list_filter =  "user", "avatar", "phone", "ticket", "date", "autres"
	ordering =  "user", "avatar", "phone", "ticket", "date", "autres"
	readonly_fields = ['ticket']

class TicketAdmin(admin.ModelAdmin):
	list_display = "ticket_type", "consommable", "autres"
	list_filter = "ticket_type", "consommable", "autres"
	ordering = "ticket_type", "consommable", "autres"

class TicketTypeAdmin(admin.ModelAdmin):
	list_display = "name", "price", "consommable"
	list_filter = "name", "price", "consommable"
	ordering = "name", "price", "consommable"

class PaymentAdmin(admin.ModelAdmin):
	list_display = "profile", "somme", "date", "autres"
	list_filter = "profile", "somme", "date", "autres"
	ordering = "profile", "somme", "date", "autres"

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
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Consommation, ConsommationAdmin)