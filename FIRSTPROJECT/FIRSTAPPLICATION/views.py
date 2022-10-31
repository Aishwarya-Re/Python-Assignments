from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import formset_factory, BaseFormSet
from .models import User
from .forms import CreateNewUser, CreateNewAddress, CreateNewContact

# Create your views here.

def index(request):
    # users = User.objects.all()
    return render(request, "FIRSTAPPLICATION/base.html", {})

def home(request, id):
    users = User.objects.filter(id=id)
    if users:
        user = users[0]
        contacts = user.contacts.all()
        addresses = user.addresses.all()
        res_di = {
            "name": user.name,
            "contacts": contacts,
            "addresses": addresses
        }
        return render(request, "FIRSTAPPLICATION/user.html", res_di)
    else:
        return render(request, "FIRSTAPPLICATION/404.html", {})

def list(request):
    users = User.objects.filter()
    if users:
        return render(request, "FIRSTAPPLICATION/list.html", {'users': users})
    else:
        return render(request, "FIRSTAPPLICATION/404.html", {})


def create(request):
    if request.method == "POST":
        form  = CreateNewUser(request.POST)
        # import pdb; pdb.set_trace()
        contacts = formset_factory(CreateNewContact)
        addresses = formset_factory(CreateNewAddress)
        # contacts.add_prefix('contacts-list-item')
        # addresses.add_prefix('addresses-list-item')
        contacts = contacts(data=request.POST)
        addresses = addresses(data=request.POST)
        form = {
            "user_form": form,
            "contact_form": contacts,
            "address_form": addresses
        }
        if False:
            n = form.cleaned_data["name"]
            u = User(name=n)
            # u.save()
            return HttpResponseRedirect("/{id}".format(id=u.id))
    elif request.method == "PUT":
        form = {}
        pass
    else:
        userForm  = CreateNewUser()
        contactForm  = formset_factory(CreateNewContact)
        addressForm  = formset_factory(CreateNewAddress)
        # import pdb; pdb.set_trace()
        # contactForm.add_prefix('contacts-list-item')
        # addressForm.add_prefix('addresses-list-item')
        form = {
            "user_form": userForm,
            "contact_form": contactForm,
            "address_form": addressForm
        }

    # import pdb; pdb.set_trace()
    return render(request, "FIRSTAPPLICATION/create.html", {"form": form})


def handle404(request, exception):
    return render(request, "FIRSTAPPLICATION/404.html")


