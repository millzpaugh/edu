from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.

SECTOR_CHOICES = (
        ('public', ('Public')),
        ('private', ('Private')),
        ('private-nonprofit', ('Private-Nonprofit')),
        ('proprietary', ('Proprietary')),
        ('foreign private', ('Foreign Private')),
        ('foreign-private', ('Foreign Private')),
        ('foreign public', ('Foreign Public')),
        ('foreign-public', ('Foreign Public')),
        ('foreign for-profit', ('Foreign For-Profit')),
        ('foreign-for-profit', ('Foreign For-Profit')),
    )

class School(models.Model):
    name = models.CharField(max_length = 200)
    state = models.CharField(max_length = 50)
    zip = models.CharField(max_length = 50)
    sector = models.CharField(max_length=30,
                                      choices=SECTOR_CHOICES,
                                      default=None)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
         """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(School, self).save(*args, **kwargs)

LOAN_TYPE_CHOICES = (
        ('dl_unsub', ('Direct Loan Unubsidized')),
        ('dl_unsub_ugrad', ('Direct Loan Unsubsidized Undergraduate')),
        ('dl_unsub_grad', ('Direct Loan Unsubsidized Graduate')),
        ('dl_parent_plus', ('Direct Loan Parent Plus')),
        ('dl_grad_plus', ('Direct Loan Grad Plus')),
        ('dl_sub_ugrad', ('Direct Loan Subsidized Undergraduate')),
        ('dl_sub_grad', ('Direct Loan Subsidized Graduate')),
    )

GRANT_TYPE_CHOICES = (
        ('pell', ('Pell Grant')),
        ('teach', ('Teach Grant Program')),
        ('iraq_afghan', ('Iraq Afghanistan Grant Program')),
    )

class Loan(models.Model):
    school_id= models.ForeignKey(School)
    loan_type = models.CharField(max_length=80,
                                      choices=LOAN_TYPE_CHOICES,
                                      default=None)
    recipients = models.IntegerField(null=True)
    number_of_loans = models.IntegerField(null=True)
    loan_money_originated = models.DecimalField(max_digits=30, decimal_places=2, null=True)
    number_of_disbursements = models.IntegerField(null=True)
    loan_money_disbursed = models.DecimalField(max_digits=30, decimal_places=2, null=True)
    year = models.IntegerField(null=False)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
         """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Loan, self).save(*args, **kwargs)

class Grant(models.Model):
    school_id= models.ForeignKey(School)
    grant_type = models.CharField(max_length=30,
                                      choices=GRANT_TYPE_CHOICES,
                                      default=None)
    recipients = models.IntegerField(null=True)
    grant_money_disbursed = models.DecimalField(max_digits=30, decimal_places=2, null=True)
    year = models.IntegerField(null=False)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
         """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Grant, self).save(*args, **kwargs)









