from django import forms
from .models import Wantoitem

class WantoitemForm(forms.ModelForm):
    class Meta:
        model = Wantoitem
        fields = ('item_name',)



