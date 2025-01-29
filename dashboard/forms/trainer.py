from django import  forms
from accounts.models import Trainer
from django.contrib.auth.hashers import make_password

class TrainerForm(forms.ModelForm):
    class Meta:
        model=Trainer
        fields=['fullName','phone','email','password']
        widgets = {
    'fullName': forms.TextInput(attrs={'class': 'form-control', }),
    'phone': forms.TextInput(attrs={'class': 'form-control', }),
    'email': forms.EmailInput(attrs={'class': 'form-control',}),
    'password': forms.PasswordInput(attrs={'class': 'form-control', }),
}
    def save(self, commit=True):
            trainer = super().save(commit=False)
            # Hash the password before saving
            trainer.password = make_password(self.cleaned_data['password'])
            if commit:
                trainer.save()
            return trainer
class TrainerUpdateForm(forms.ModelForm):
    class Meta:
        model=Trainer
        fields=['fullName','phone','email',]
        widgets = {
    'fullName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
    'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
    'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
}