from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request):
    context = {
    "API_NAME": "TRADING API",
    "ENDPOINTS": ["api/stocks", "api/customer", "api/order", "api/login", "api/logout", "api/customer/<str:id>"]
    }  

    return Response(context, status=status.HTTP_200_OK)