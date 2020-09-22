from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import *
from .serializers import *

class TokenPairView(TokenObtainPairView):
	serializer_class = TokenPairSerializer

class ProfileViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, JWTAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

class TicketViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, JWTAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Ticket.objects.all()
	serializer_class = TicketSerializer

class PaymentViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, JWTAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Payment.objects.all()
	serializer_class = PaymentSerializer

class ProductViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, JWTAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class ConsommationViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, JWTAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Consommation.objects.all()
	serializer_class = ConsommationSerializer

	# @action(methods=['GET'], detail=False,
	# 	url_path=r'quantite/(?P<produit_id>[0-9]+)',
	# 	url_name="quantite_total")
	# def quantiteTotal(self, request, produit_id):
	# 	produit = Produit.objects.get(id=produit_id)
	# 	return Response({'quantite':produit.quantiteEnStock()})