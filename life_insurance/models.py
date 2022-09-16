from django.db import models
from django.forms.widgets import DateInput

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)
    email = models.EmailField(unique=True)


class Agent(models.Model):
    agent_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Bank(models.Model):
    bank_name = models.CharField(max_length=255)
    bank_location = models.CharField(max_length=255)
    bank_address = models.CharField(max_length=255)
    branch_code = models.CharField(max_length=255)

class Bank_Account(models.Model):
    account_no = models.CharField(max_length=10)
    type_of_account = models.CharField(max_length=255)

class Policy_Bond(models.Model):
    POLICY_TYPE_INDIVIDUAL_POLICY = 'IP'
    POLICY_TYPE_FAMILY_POLICY = 'FP'
    POLICY_TYPE_GROUP_POLICY = 'GP'

    POLICY_TYPE_CHOICES = [
        (POLICY_TYPE_INDIVIDUAL_POLICY, 'Individual Policy'),
        (POLICY_TYPE_FAMILY_POLICY, 'Family Policy'),
        ( POLICY_TYPE_GROUP_POLICY , 'Group Policy'),
    ]

    policy_no = models.IntegerField()
    policy_type = models.CharField(max_length=255, choices=POLICY_TYPE_CHOICES, default= POLICY_TYPE_INDIVIDUAL_POLICY )
    amount_of_policy = models.DecimalField(max_digits=6, decimal_places=2)
    premium_amount = models.DecimalField(max_digits=6, decimal_places=2)


class New_Business(models.Model):
    officer_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    start_date = models.DateField(auto_now=True)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)



