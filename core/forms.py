from django import forms
from .models import Notes

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'

# ['subject','topic','about','remark','docs','slug']