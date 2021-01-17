from enum import unique
from django.db import models
from backend.utils import id_generator

class SalesPerson(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    phone = models.BigIntegerField(blank=True, null=True, unique=True)
    employee_id = models.CharField(primary_key=True, max_length=20, unique=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)



class Leads(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    organizatioin = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    phone = models.BigIntegerField(blank=True, null=True, unique=True)
    source_of_leads = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    type_of_interaction = models.CharField(max_length=100, blank=True, null=True)
    date_of_interaction = models.DateField(blank=True, null=True)
    time_of_interaction = models.CharField(max_length=50, blank=True, null=True)
    interaction_detail = models.TextField(blank=True, null=True)
    score = models.CharField(max_length=50, blank=True, null=True)
    assign_to = models.ForeignKey(SalesPerson, blank=True, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name