from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
	path("", Home.as_view(), name="home"),
	path("edit/<int:profile_id>/", EditProfile.as_view(), name="editprofile"),
	path("delete/<int:profile_id>/", DeleteProfile.as_view(), name="deleteprofile"),
	path("login/", Connexion.as_view(), name="login"),
	path("logout/", deconnexion, name="logout"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

