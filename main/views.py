from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import ListAPIView 
from django.utils.decorators import decorator_from_middleware
from .middleware import RequestMiddleware
from .serializers import FormulaValidationSerializer, LoggerSerializer
from .models import Logger



@api_view(['POST'])
def check_formula_view(request):
    if request.method == 'POST':
        serializer = FormulaValidationSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'formula': True}, status=status.HTTP_200_OK)
        else:
            return Response({'formula': False}, status=status.HTTP_400_BAD_REQUEST)


class RequestLogList(ListAPIView):
    queryset = Logger.objects.all()
    serializer_class = LoggerSerializer
