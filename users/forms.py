from django import forms
from .models import User

class UserCreationForm(forms.ModelForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False)
    user_type = forms.ChoiceField(required=True,choices=User.choices)
    password = forms.CharField(
        widget = forms.PasswordInput()
    )


    class Meta:
        model = User
        fields = ('name','email','phone','password','user_type')

    