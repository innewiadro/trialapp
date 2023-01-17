from django.db.transaction import atomic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.forms import CharField, Textarea, TextInput, IntegerField
from django.db.models import TextField
from .models import Profile
from django import forms


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = "form-control"


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ["username", "first_name", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visable in self.visible_fields():
            visable.field.widget.attrs["class"] = "form-control"

    @atomic
    def save(self, commit=True):
        self.instance_is_active = False
        user = super().save(commit)
        
        profile = Profile(user=user)
        if commit:
            profile.save()
        return super().save(commit)


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ["username", "first_name", "last_name", "email"]

    
 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["title", "contact_number"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


            
        

  
    
