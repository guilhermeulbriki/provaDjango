from django.contrib import admin
from django.urls import path
from prova import views
from medicos import views as medicoView
from pacientes import views as pacienteView

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('medicos/', medicoView.index),
    path('medicos/<int:id>', medicoView.infoMedicos, name='infoMedicos'),
    path('pacientes/', pacienteView.index),
    path('pacientes/<int:id>', pacienteView.infoPacientes, name='infoPacientes'),
]
