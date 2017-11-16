from django.contrib import admin
from .models import Customer, Mortgage
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'account_customer', 'fullname', 'cell', 'created')

@admin.register(Mortgage)
class Mortgage(admin.ModelAdmin):
    list_display = ('id', 'customer_mortgage', 'loan_amount', 'loan_begin', 'loan_rate', 'loan_model')