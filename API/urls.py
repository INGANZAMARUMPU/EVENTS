from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from .api import *

router = routers.DefaultRouter()
router.register("profile", ProfileViewset)
router.register("ticket", TicketViewset)
router.register("payment", PaymentViewset)
router.register("product", ProductViewset)
router.register("consommation", ConsommationViewset)
router.register("event", EventViewset)

urlpatterns = [
	path("", include(router.urls)),
    path('login/', TokenPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]
