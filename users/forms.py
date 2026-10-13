from django import forms
from .models import SUser
from django.contrib.auth.hashers import make_password


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label=" Password ",widget=forms.PasswordInput)
    confirm_password = forms.CharField(label=" Confirm Password ",widget=forms.PasswordInput)

    class Meta:
        model = SUser
        fields = "__all__"


    def clean_confirm_password(self):
        password = self.cleaned_data.get("password") 
        confirm_password = self.cleaned_data.get("confirm_password")   

        if password and confirm_password and password != confirm_password :
            raise forms.ValueError(" Password doesn't Match !!!")
        return confirm_password

    def __init__(self, *args, **kwargs):
            self.request = kwargs.pop('request', None)
            super().__init__(*args, **kwargs)
    
            # If not logged in: only allow customer or store_admin
            if not self.request or not self.request.user.is_authenticated:
                self.fields['role'] = "passenger"
            else:
                pass

    def save(self, commit=True):
            user = super().save(commit=False)
    
            user.password = make_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user        
    

class EmailUserLoginForm(forms.ModelForm):
     class Meta :
          model = SUser
          fields = ["email","password"]
    


class UserEditForm(forms.ModelForm):
     class Meta :
          model = SUser
          fields = ["first_name","last_name","email","national_id","passport_id","phone"]
    


