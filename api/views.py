from django.contrib.auth import login
from .serializer import *
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal

#===============================================================
#class-based views for login/logout

class LoginAPI(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

#===============================================================
#function based views for api endpoints

@api_view(['GET'])
def get_all_stock(request):

    if request.method == 'GET':
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        context = {'stocks':serializer.data}
        return Response(context, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])    
def get_customer_portfolio(request):
    customer = request.user.customer
    if request.method == 'GET':
        context = {
            'name': customer.name,
            'portfolio value': customer.valuation,
        }
        return Response(context, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated]) 
def get_customer_specific_stock(request, id):
    customer = request.user.customer
    try:
        stock = Stock.objects.get(stock_id = id)
        stocks = PurchaseOrder.objects.filter(customer=customer, stock=stock)
    except PurchaseOrder.DoesNotExist and Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(stocks, many=True)
        print(serializer.data)
        for items in serializer.data:
            print(items['price'])
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated]) 
def process_order(request):
    customer = request.user.customer

    if request.method == 'POST':
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            try:
                stock = Stock.objects.get(stock_id=serializer.data['stock_id'])
            except Stock.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            if stock.price * serializer.data['stock_qty'] == abs(Decimal(serializer.data['price'])):
                result = process_buy_sell(customer=customer, stock=stock, serializer=serializer)
                if result:
                    context = {
                        'customer': customer.name,
                        'stock': stock.name,
                        'stock_qty': serializer.data['stock_qty'],
                        'price': serializer.data['price'],
                    }
                    return Response(context, status=status.HTTP_201_CREATED)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


def process_buy_sell(customer, stock, serializer):
    client_price = Decimal(serializer.data['price'])
    if client_price > 0:
        PurchaseOrder.objects.create(customer=customer, stock=stock, stock_qty=serializer.data['stock_qty'], 
                    price=client_price)
        customer.update_valuation(Decimal(client_price))
        customer.save()
        return True

    elif client_price < 0:
        try:
            prev_stock = PurchaseOrder.objects.filter(customer=customer, stock=stock)
        except PurchaseOrder.DoesNotExist:
            return False

        serialized_data = OrderSerializer(prev_stock, many=True)
        prev_total = sum([Decimal(items['price']) for items in serialized_data.data])

        if prev_total >= abs(client_price):
            PurchaseOrder.objects.create(customer=customer, stock=stock, stock_qty=serializer.data['stock_qty'], 
                    price=client_price)
            customer.update_valuation(Decimal(serializer.data['price']))
            customer.save()
            return True
        
        else:
            return False
    else:
        return False


