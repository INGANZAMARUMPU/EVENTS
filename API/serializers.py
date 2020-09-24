from .models import *
from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ProfileSerializer(serializers.ModelSerializer):
	fullname = serializers.SerializerMethodField()

	def get_fullname(self, obj):
		return f"{obj.user.first_name} {obj.user.last_name}"

	class Meta:
		model = Profile
		fields = "fullname", "avatar", "phone", "mobile", "date", "ticket", "autres", "qr"
		depth = 1;

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

class TokenPairSerializer(TokenObtainPairSerializer):
	
	@classmethod
	def get_token(cls, user):
		token = super(TokenPairSerializer, cls).get_token(user)
		try:
			token['username'] = user.username
			token['phone'] = user.profile.phone
			token['mobile'] = user.profile.mobile
			token['services'] = [group.name for group in user.groups.all()]
		except :
			print
		return token