from django.forms  import ModelForm
from .models import Tarea

class TareasForm(ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'important']