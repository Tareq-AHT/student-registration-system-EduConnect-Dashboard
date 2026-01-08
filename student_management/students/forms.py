from django import forms

class StudentRegistrationForm(forms.Form):
    
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={
            'style': 'width: 100%; background: transparent; border: none; border-bottom: 1px solid #4a5568; color: white; padding: 10px 0; outline: none; font-size: 15px;',
            'placeholder': 'Enter UserName',
            'autocomplete': 'off'
        })
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'style': 'width: 100%; background: transparent; border: none; border-bottom: 1px solid #4a5568; color: white; padding: 10px 0; outline: none; font-size: 15px;',
            'placeholder': 'Enter Email',
            'autocomplete': 'off'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'style': 'width: 100%; background: transparent; border: none; border-bottom: 1px solid #4a5568; color: white; padding: 10px 0; outline: none; font-size: 15px;',
            'placeholder': 'Enter Password',
            'autocomplete': 'new-password'
        })
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'style': 'width: 100%; background: transparent; border: none; border-bottom: 1px solid #4a5568; color: white; padding: 10px 0; outline: none; font-size: 15px;',
            'placeholder': 'Confirm Password',
            'autocomplete': 'new-password'
        })
    )