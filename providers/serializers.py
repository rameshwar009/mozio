from .models import Provider, ProviderPolygon
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'

    def create(self, validated_data):
        return Provider.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get(
            'phone_number', instance.phone_number)
        instance.language = validated_data.get('language', instance.language)
        instance.currency = validated_data.get('currency', instance.currency)
        instance.save()
        return instance


class PolygonSerializer(GeoFeatureModelSerializer):
    provider_name = serializers.SerializerMethodField()

    class Meta:
        model = ProviderPolygon
        geo_field = 'poly'
        fields = ('polygon_name', 'price', 'provider_name', 'provider')

    def update(self, instance, validated_data):
        instance.polygon_name = validated_data.get(
            'polygon_name', instance.polygon_name)
        instance.price = validated_data.get('price', instance.price)
        instance.provider = validated_data.get('provider', instance.provider)
        instance.poly = validated_data.get('poly', instance.poly)
        instance.save()
        return instance

    def get_provider_name(self, obj):
        return obj.provider.name
