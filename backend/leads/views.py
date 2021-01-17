from django.db import models
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import SalesPerson, Leads
from .serializers import SalesPersonSerializer, LeadSerializer
from backend.utils import id_generator


class SalesPersonView(viewsets.ModelViewSet):
    queryset = SalesPerson.objects.all()
    serializer_class = SalesPersonSerializer

    def perform_create(self, serializer):
        employeeID = id_generator()
        serializer.save(employee_id = employeeID)

    def destroy(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(SalesPerson, employee_id=pk)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class LeadView(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadSerializer