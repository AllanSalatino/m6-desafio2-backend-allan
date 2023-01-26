from django.urls import path
from . import views

urlpatterns = [
    path("trasacoes/", views.TransacaoView.as_view()),
    path("trasacoes/<str:cpf>/", views.TransacaoDetailView.as_view()),
]