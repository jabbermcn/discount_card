from datetime import datetime, timedelta

import pytz
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializers import *
from discount.models import *


class ExpiredTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        user, token = super(ExpiredTokenAuthentication, self).authenticate_credentials(key=key)
        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)
        if (token.created + timedelta(minutes=2)) < utc_now:
            raise AuthenticationFailed('token has expired')
        return user, token


class CardStatusViewSet(ModelViewSet):
    queryset = CardStatus.objects.all()
    serializer_class = CardStatusSerializer
    authentication_classes = [ExpiredTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class CardSeriesViewSet(ModelViewSet):
    queryset = CardSeries.objects.all()
    serializer_class = CardSeriesSerializer
    authentication_classes = [ExpiredTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    authentication_classes = [ExpiredTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [ExpiredTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [ExpiredTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class OrderProductViewSet(ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
    authentication_classes = [ExpiredTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class ExpiredObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            pass
        else:
            token.delete()
        token = Token(
            user=user,
            created=datetime.now()
        )
        token.save()
        return Response({'token': token.key})


expired_obtain_auth_token = ExpiredObtainAuthToken.as_view()
