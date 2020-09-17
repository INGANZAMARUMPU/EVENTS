from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
	list_display = "user", "avatar", "phone", "mobile", "ticket", "date", "autres"
	list_filter =  "user", "avatar", "phone", "mobile", "ticket", "date", "autres"
	ordering =  "user", "avatar", "phone", "mobile", "ticket", "date", "autres"
class TicketAdmin(admin.ModelAdmin):
	list_display = "name", "somme", "consommable", "autres"
	list_filter = "name", "somme", "consommable", "autres"
	ordering = "name", "somme", "consommable", "autres"
class PaymentAdmin(admin.ModelAdmin):
	list_display = "profile", "somme", "date", "autres"
	list_filter = "profile", "somme", "date", "autres"
	ordering = "profile", "somme", "date", "autres"
class ProductAdmin(admin.ModelAdmin):
	list_display = "name", "price"
	list_filter ="name", "price"
	ordering ="name", "price"
class ConsommationAdmin(admin.ModelAdmin):
	list_display = "product" ,"profile" ,"when" 
	list_filter = "product" ,"profile" ,"when" 
	ordering = "product" ,"profile" ,"when" 

# class DetailCommandeAdmin(admin.ModelAdmin):
# 	list_display = ("recette", "commande", "quantite", "somme", "date")
# 	list_filter = ("recette", "commande", "quantite", "somme", "date")
# 	search_field = ("recette", "commande", "quantite", "somme", "date")
# 	ordering = ("recette", "commande", "quantite", "somme", "date")

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Consommation, ConsommationAdmin)