from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts")
    contact_type = models.CharField(max_length=10,
        choices=[('Email', 'Email'), ('Phone', 'Phone')], null=False, blank=False)
    contact_at = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return "{_type}: {contact}".format(
            _type=self.contact_type, contact=self.contact_at)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    address_type = models.CharField(max_length=10,
        choices=[('Home', 'Home'), ('Office', 'Office')], null=False, blank=False)
    house_number = models.CharField(max_length=20, null=False, blank=False)
    address_line_1 = models.CharField(max_length=100, null=False, blank=False)
    address_line_2 = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=30, null=False, blank=False)
    zipcode = models.IntegerField(null=False, blank=False)
    country = models.CharField(max_length=30)

    def __str__(self):
        return ("Address: {h_no}\n{add_1},\n{add_2},\n{city} - {zip},\n{country}".format(
            h_no=self.house_number, add_1=self.address_line_1,
            add_2=self.address_line_2, city=self.city, zip=self.zipcode,
            country=self.country))
