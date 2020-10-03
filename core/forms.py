from django import forms
from .models import Notes,Subject

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
        widgets = {
            'subject': forms.Select(attrs={'class':'form-control','placeholder':'Select Subject'}),
            'topic': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Topic'}),
            'about': forms.TextInput(attrs={'class':'form-control','placeholder':'About'}),
            'remark': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Remark'}),
            'docs': forms.FileInput(attrs={'class':'form-control','placeholder':'Upload File'}),
            'slug': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Subject Code (lowercase)'})
        }

class SearchForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['department']
        widgets = {
            'department': forms.Select(attrs={'class':'form-control','placeholder':'Select Department'})
        }

class ClassSearchForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['subject']
        widgets = {
            'subject': forms.Select(attrs={'class':'form-control','placeholder':'Select Subject'})
        }

class ClassUpdateForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['starttime','stoptime','meetlink']
        widgets = {
            'starttime': forms.Select(attrs={'class':'form-control','placeholder':'Select Subject'}),
            'stoptime': forms.Select(attrs={'class':'form-control','placeholder':'Select Subject'}),
            'meetlink': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Meet Link'})
        }
# ['subject','topic','about','remark','docs','slug']