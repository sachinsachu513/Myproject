from django.urls import path
from . import views
urlpatterns = [
  path('buzz/',views.fetch_cricket_scores),
    path('buss/',views.fetch_upcoming_matches),


]