from django import forms

class DonorForm(forms.Form):
    
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=19, label='Age')
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    sex = forms.ChoiceField(choices=SEX_CHOICES)
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    blood_group = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES)
    mobile_number = forms.CharField(max_length=15)
    email = forms.EmailField()
    diseases = forms.CharField(max_length=200)
    donor_organ = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
