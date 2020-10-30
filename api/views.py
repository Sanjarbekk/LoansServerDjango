from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from .models import Loan
from .serializers import LoanSerializer
from rest_framework.views import APIView


# Create your views here.

class LoanAPIView(APIView):

    def get(self, request):
        loans = Loan.objects.all()
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)


class LoanAPIAdd(APIView):

    def post(self, request):
        serializer = LoanSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            loans = Loan.objects.all()
            serializer = LoanSerializer(loans, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoanDetails(APIView):
    def get_object(self, uid):
        try:
            return Loan.objects.get(uid=uid)

        except Loan.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, uid):
        loans = self.get_object(uid)
        serializer = LoanSerializer(loans)
        return Response(serializer.data)

    def put(self, request, uid):
        loans = self.get_object(uid)
        serializer = LoanSerializer(loans, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uid):
        loans = self.get_object(uid)
        loans.delete()
        loans1 = Loan.objects.all()
        serializer = LoanSerializer(loans1, many=True)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
