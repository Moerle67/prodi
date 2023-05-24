from django import forms

from .models import *

# class MyBaseForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control bs-3'
    
#     @staticmethod
#     def liste(eingabe):
#         liste = []
#         for zeile in eingabe:
#             liste.append((zeile.id, zeile))
#         return liste

# class NameForm(MyBaseForm):
#     your_name = forms.CharField(label='Your name', max_length=100, help_text="Name eingeben")
#     s_woerter = Schlagwort.objects.all()
#     schlagwort = forms.ChoiceField(choices=MyBaseForm.liste(s_woerter), label="Wert")
#     your_pass = forms.CharField(label="Passwort", max_length=50, required=False)

# class UploadFileForm(forms.Form):
#     # title = forms.CharField(max_length=50)
#     file = forms.FileField()