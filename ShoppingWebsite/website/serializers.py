from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *



class ProductsSerializer(serializers.ModelSerializer):
    # Defining a serializer class named ArticleSerializer that
    # inherits from
    # serializers.ModelSerializer. This class is used to convert complex data types (like Django models) into Python
    # data types that can be easily rendered into JSON.
    class Meta:
        model = Products
        fields = ['ID',  'Name', 'price']

    def validate(self, attrs):
        unknown = set(self.initial_data) - set(self.fields)
        if unknown:
            raise ValidationError("Unknown field(s): {}".format(", ".join(unknown)))
        return attrs