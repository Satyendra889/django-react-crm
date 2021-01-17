from django.db.models import fields
from .models import Leads, SalesPerson
from rest_framework import serializers


class SalesPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesPerson
        fields = "__all__"
        read_only_fields = ("employee_id",)

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = "__all__"