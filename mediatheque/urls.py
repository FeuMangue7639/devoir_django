from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bibliotheque/', include('bibliotheque.urls', namespace='bibliotheque')),
    path('emprunteur/', include('emprunteur.urls', namespace='emprunteur')),
    path('', RedirectView.as_view(url='/bibliotheque/', permanent=False)),
]

