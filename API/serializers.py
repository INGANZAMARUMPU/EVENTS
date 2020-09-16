from .models import *
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
	fullname = serializers.SerializerMethodField()

	def get_fullname(self, obj):
		return f"{obj.user.first_name} {obj.user.last_name}"

	class Meta:
		model = Profile
		fields = "__all__"

class TicketSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticket
		fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Payment
		fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = "__all__"

class ConsommationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Consommation
		fields = "__all__"

# class DetailCommandeSerializer(serializers.ModelSerializer):
# 	nom = serializers.SerializerMethodField()
# 	def get_nom(self, obj):
# 		return obj.recette.nom

# 	class Meta:
# 		model = DetailCommande
# 		fields = "id", "quantite", "somme", "pret", "commande", "recette", 'nom', 'obligations'