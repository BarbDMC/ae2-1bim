from django import forms
from .models import ParqueNatural, GuiaTuristico, Recorrido

class ParqueForm(forms.ModelForm):
    class Meta:
        model = ParqueNatural
        fields = '__all__'

class GuiaForm(forms.ModelForm):
    class Meta:
        model = GuiaTuristico
        fields = '__all__'

class RecorridoForm(forms.ModelForm):
    class Meta:
        model = Recorrido
        fields = '__all__'
