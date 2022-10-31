from django.forms import ModelForm
from .models import User, Contact, Address

class CreateNewUser(ModelForm):
    class Meta:
        model = User
        fields = ['name']

class CreateNewContact(ModelForm):
    class Meta:
        model = Contact
        exclude = ['id', 'user']

class CreateNewAddress(ModelForm):
    class Meta:
        model = Address
        exclude = ['id', 'user']
