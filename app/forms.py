from django import forms
from .models import RetailData

class CsvUploadForm(forms.Form):
    csv_file = forms.FileField (
        label = 'CSV File',
        help_text = 'Upload a CSV file (columns must include merchant, sku, and country)'
    )

class AnnotationForm(forms.ModelForm):
    class Meta:
        model = RetailData
        fields = ['retailer', 'segment']
        widgets = {
            'retailer': forms.TextInput(attrs = {'class': 'form-control'}),
            'segment': forms.Select(attrs = {'class': 'form-control'}),
        }