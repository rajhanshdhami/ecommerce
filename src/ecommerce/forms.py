from django import forms

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
    username=      
