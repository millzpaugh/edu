from django.db import models

# Create your models here.

SECTOR_CHOICES = (
        ('public', ('Public')),
        ('private-nonprofit', ('Private-Nonprofit')),
        ('proprietary', ('Proprietary')),
    )

class School(models.Model):
    name = models.CharField(max_length = 200)
    state = models.CharField(max_length = 50)
    zip = models.IntegerField(max_length = 50)
    sector = models.CharField(max_length=30,
                                      choices=SECTOR_CHOICES,
                                      default=None)

LOAN_TYPE_CHOICES = (
        ('dl_sub_ugrad', ('Direct Loan Subsidized Undergraduate')),
        ('dl_unsub_ugrad', ('Direct Loan Unsubsidized Undergraduate')),
        ('dl_sub_grad', ('Direct Loan Subsidized Graduate')),
        ('dl_unsub_grad', ('Direct Loan Unsubsidized Graduate')),
        ('dl_parent_plus', ('Direct Loan Parent Plus')),
        ('dl_grad_plus', ('Direct Loan Grad Plus')),
    )

GRANT_TYPE_CHOICES = (
        ('pell', ('Pell Grant')),
        ('teach', ('Teach Grant Program')),
        ('iraq_afghan', ('Iraq Afghanistan Grant Program')),
    )

class Loan(models.Model):
    school_id= models.ForeignKey(School)
    loan_type = models.CharField(max_length=2,
                                      choices=LOAN_TYPE_CHOICES,
                                      default=None)
    recipients = models.IntegerField(null=True)
    number_of_loans = models.IntegerField(null=True)
    loan_money_originated = models.DecimalField(max_digits=30, decimal_places=2, null=True)
    number_of_disbursements = models.IntegerField()
    loan_money_disbursed = models.DecimalField(max_digits=30, decimal_places=2, null=True)
    year = models.IntegerField(null=False)

class Grant(models.Model):
    school_id= models.ForeignKey(School)
    grant_type = models.CharField(max_length=30,
                                      choices=GRANT_TYPE_CHOICES,
                                      default=None)
    recipients = models.IntegerField(null=True)
    grant_money_disbursed = models.DecimalField(max_digits=30, decimal_places=2, null=True)
    year = models.IntegerField(null=False)









