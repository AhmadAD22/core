from django import  forms
from accounts.models import Manager
from django.contrib.auth.hashers import make_password

class ManagerForm(forms.ModelForm):
    class Meta:
        model=Manager
        fields=['fullName','phone','email','password']
        widgets = {
    'fullName': forms.TextInput(attrs={'class': 'form-control', }),
    'phone': forms.TextInput(attrs={'class': 'form-control', }),
    'email': forms.EmailInput(attrs={'class': 'form-control',}),
    'password': forms.PasswordInput(attrs={'class': 'form-control', }),
}
    def save(self, commit=True):
            manager = super().save(commit=False)
            # Hash the password before saving
            manager.password = make_password(self.cleaned_data['password'])
            manager.is_staff=True
            
            if commit:
                manager.save()
            return manager
        
        
class ManagerUpdateForm(forms.ModelForm):
    class Meta:
        model=Manager
        fields=['fullName','phone','email',]
        widgets = {
    'fullName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
    'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
    'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
}