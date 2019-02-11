import django.forms as forms
from django.db import models

class ChoiceFieldNoValidation(forms.ChoiceField):
    def validate(self, value):
        pass

class QueryForm(forms.Form):
    detalle = models.CharField(max_length=200)
    criterio = models.CharField(max_length=200)

    """class Meta:
        model = User
        fields = ('username','password','nombre','rut','cargo')"""

QueryFormSet = forms.formset_factory(QueryForm, can_delete=True)