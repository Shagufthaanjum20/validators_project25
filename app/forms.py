

from django import forms



def check_for_a(value):
    if value[0]=='s':
        raise forms.validationError('name starts with s')
        
class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[check_for_a])    
    Sage=forms.IntegerField()
    Sid=forms.IntegerField()