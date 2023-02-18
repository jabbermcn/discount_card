from rest_framework.serializers import ModelSerializer

from discount.models import *


class CardStatusSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data.update(validated_data.get('name') + ' ' + str(validated_data.get('id')))
        post = CardStatus(**validated_data)
        post.save()
        return post

    class Meta:
        model = CardStatus
        fields = ('name',)


class CardSeriesSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data.update(validated_data.get('name') + ' ' + str(validated_data.get('id')))
        post = CardSeries(**validated_data)
        post.save()
        return post

    class Meta:
        model = CardSeries
        fields = ('name',)


class CardSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data.update(validated_data.get('card_number') + ' ' + str(validated_data.get('id')))
        post = Card(**validated_data)
        post.save()
        return post

    class Meta:
        model = Card
        fields = (
            'card_number', 'status', 'series', 'date_created', 'expire_date', 'last_used_date', 'total', 'discount',
        )


class ProductSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data.update(validated_data.get('name') + ' ' + str(validated_data.get('id')))
        post = Product(**validated_data)
        post.save()
        return post

    class Meta:
        model = Product
        fields = (
            'name', 'price', 'discount',
        )


class OrderSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data.update(validated_data.get('card') + ' ' + str(validated_data.get('id')))
        post = Order(**validated_data)
        post.save()
        return post

    class Meta:
        model = Order
        fields = (
            'date_created', 'card',
        )


class OrderProductSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data.update(validated_data.get('order') + ' ' + str(validated_data.get('id')))
        post = OrderProduct(**validated_data)
        post.save()
        return post

    class Meta:
        model = OrderProduct
        fields = (
            'discount', 'product', 'order',
        )
