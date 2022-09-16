from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Policy_Bond)
class policy_bond(admin.ModelAdmin):
    list_display = ['policy_type', 'policy_no', 'amount_of_policy','premium_amount']
    list_editable = ['amount_of_policy', 'policy_no']
