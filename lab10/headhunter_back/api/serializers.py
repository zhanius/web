from rest_framework import serializers

from .models import *

# class CompanySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)
#     description = serializers.CharField()
#     city = serializers.CharField(max_length=255)
#     address = serializers.CharField()
#
#     class Meta:
#         model = Company
#         fields = ['name', 'description', 'city', 'address']
#         extra_kwargs = {
#             'name': {'required': False},
#             'description': {'required': False},
#             'city': {'required': False},
#             'address': {'required': False}
#         }
#
#     def create(self, validated_data):
#         instance = Company.objects.create(
#             name = validated_data.get('name'),
#             description = validated_data.get('description'),
#             city = validated_data.get('city'),
#             address = validated_data.get('address')
#         )
#         return instance
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name')
#         instance.description = validated_data.get('description')
#         instance.city = validated_data.get('city')
#         instance.address = validated_data('address')
#         instance.save()
#         return instance



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address')

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id','name','description','salary','company')


