from django.db import models
from django.utils import timezone
from account.models import Account
from datetime import datetime

class Customer(models.Model):

    account_customer = models.ForeignKey(
        Account, null=True, blank=True
    )
    fullname = models.CharField(max_length=100, blank=True, default='')
    cell = models.CharField(max_length=11, blank=False, default='', unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Name:{0} Cell:{1}'.format(self.fullname, self.cell)

    class Meta:
        ordering = ('created',)

class Mortgage(models.Model):

    LOAN_MODEL_CHOICS = (
        ('BI','Before_Interest'),
        ('EP','Equal_Principal')
    )

    customer_mortgage = models.ForeignKey(
        Customer, on_delete=models.CASCADE
    )
    loan_amount = models.FloatField(max_length=100, blank=False)
    loan_begin = models.DateTimeField(auto_now_add=False, blank=False, default=timezone.now)
    loan_end = models.DateTimeField(auto_now_add=False, blank=False, default=timezone.now)
    loan_rate = models.DecimalField(max_digits=5,decimal_places=3, default=0.03)
    loan_model = models.CharField(
        max_length=2,
        choices=LOAN_MODEL_CHOICS,
        default='BI',
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('loan_end',)

class SMS(models.Model):
    customer_sms_sent = models.ForeignKey(Customer, blank=True, null=True)
    sms = models.CharField(max_length=100, blank=True, default='')
    sms_status = models.CharField(
        max_length = 5,
        choices = (('True', 'The sms is sent'), ('False', 'Sent failed')),
        default='False'
    )