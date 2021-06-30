from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class" : "form-control",
                "id" : "form-full-name",
                "placeholder" : "Name",
                "name" : "full_name"
            }
        )
    )
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs= {
                "class" : "form-control",
                "id" : "form_email",
                "placeholder" : "email",
                "name" : "email"
            }
        )
    )
    content = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                "class" : "form-control",
                "id" : "form_content",
                "placeholder" : "your content",
                "name" : "content"
            }
        )
    )
    #for extra validation we created the clean methods for particular fields
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email

class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class" : "form-control",
                "id" : "form-full-name",
                "placeholder" : "Name",
                "name" : "user_name"
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "class" : "form-control",
                "id" : "form_pass_id",
                "placeholder" : "Password" ,
                "name" : "password"
            }
        )
    )

class RegisterForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class" : "form-control",
                "id" : "form_full_name",
                "placeholder" : "Name",
                "name" : "user_name"
            }
        )
    )      
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs= {
                "class" : "form-control",
                "id" : "form_email",
                "placeholder" : "email",
                "name" : "email"
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "class" : "form-control",
                "id" : "form_pass_id",
                "placeholder" : "Password" ,
                "name" : "password"
            }
        )
    )
    confirm_password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "class" : "form-control",
                "id" : "form_pass_id",
                "placeholder" : "Password" ,
                "name" : "confirm_password"
            }
        )
    )
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.existes():
            raise forms.ValidationError("email is taken")
        return email    

    def clean(self):
        data = self.cleaned_data
        print(data)
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Password must match")
        else:
            print("password matches")
            

        return data          
