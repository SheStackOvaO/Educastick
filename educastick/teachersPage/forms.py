from django.forms import ModelForm
from teachersPage import models

class TypeGroupForm(ModelForm):
    class Meta:
        model = models.TypeGroup
        fields = ('name',)

class SubjectForm(ModelForm):
    class Meta:
        model = models.Subject
        fields = ('name',)

# class TestForm(ModelForm.Form):
#     img = ModelForm.ImageField()
