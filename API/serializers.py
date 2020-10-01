from .models import *
from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class TicketSerializer(serializers.ModelSerializer):
	name = serializers.SerializerMethodField()
	price = serializers.SerializerMethodField()

	def get_name(self, obj):
		return f"{obj.ticket_type.name}"

	def get_price(self, obj):
		return f"{obj.ticket_type.price}"

	class Meta:
		model = Ticket
		fields = "id", "name", "price", "consommable", "autres"

class ProfileSerializer(serializers.ModelSerializer):
	fullname = serializers.SerializerMethodField()
	email = serializers.SerializerMethodField()
	ticket = TicketSerializer(many=False, read_only=True)

	def get_fullname(self, obj):
		return f"{obj.user.first_name} {obj.user.last_name}"

	def get_email(self, obj):
		return f"{obj.user.email}"

	class Meta:
		model = Profile
		fields = "id", "fullname", "avatar", "phone", "email", "date", "ticket", "autres", "qr"
		depth = 1

class PaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Payment
		fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = "__all__"

class ConsommationSerializer(serializers.ModelSerializer):
	total = serializers.SerializerMethodField()

	def get_total(self, obj):
		return obj.quantity*obj.product.price

	class Meta:
		model = Consommation
		fields = "__all__"

class TokenPairSerializer(TokenObtainPairSerializer):
	
	@classmethod
	def get_token(cls, user):
		token = super(TokenPairSerializer, cls).get_token(user)
		token['services'] = [group.name for group in user.groups.all()]
		try:
			token['username'] = user.username
			token['phone'] = user.profile.phone
			token['email'] = user.email
		except Exception as e:
			print(e)
		return token