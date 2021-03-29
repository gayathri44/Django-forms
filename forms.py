from django import forms  
class VehicleForm(forms.Form):  
    shipments = forms.IntegerField(label="Enter no of shipments")  
    weights  = forms.CharField(label="Enter weights") 
    