from django import  forms
from accounts.models import Student
from django.contrib.auth.hashers import make_password

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['fullName','phone','email','password']
        widgets = {
    'fullName': forms.TextInput(attrs={'class': 'form-control', }),
    'phone': forms.TextInput(attrs={'class': 'form-control', }),
    'email': forms.EmailInput(attrs={'class': 'form-control',}),
    'password': forms.PasswordInput(attrs={'class': 'form-control', }),
}
    def save(self, commit=True):
            student = super().save(commit=False)
            # Hash the password before saving
            student.password = make_password(self.cleaned_data['password'])
            if commit:
                student.save()
            return student
        
        
class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['fullName','phone','email',]
        widgets = {
    'fullName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
    'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
    'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
}